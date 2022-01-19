import requests
import json
import datetime
import pause
import time
import math
import numpy as np
import os

header = {
            "Authorization": "OTIwOTUwMTE3MjI4NDkwNzky.YdTofw.3dot1Af3IkNxt36P2RUOp0Hqcc4",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

channel_id = 917959442253893664

def init():

    token = os.environ['Token']
    channel_id = os.environ['Channel_Id']
    if not token:
        raise Exception('empty token')
    
    if not channel_id:
        raise Exception('empty channel id')


    header['Authorization'] = token
    channel_id = channel_id

    return channel_id

def sendMessage(channel_id,message): 
    # msg = {
    #         "content": "!rank"
    # }
    msg = {
            "content": message
    }
    
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    try:
        res = requests.post(url=url, headers=header, data=json.dumps(msg))

    except:
        pass

    return res

def deleteMessage(channel_id,message_id): 
    
    url = "https://discord.com/api/v9/channels/{}/messages/{}".format(channel_id,message_id)
    try:
        res = requests.delete(url=url, headers=header)

    except:

        pass

    return message_id

def getMessages(channel): 
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel)
    try:
        res = requests.get(url=url, headers=header)

        data = res.json()
    except:
        pass
    return data

def getCurrentUser():
    url = "https://discord.com/api/v9/users/@me"
    try:
        res = requests.get(url=url, headers=header)

        data = res.json()
    except:
        pass

    return data


def delay(minutes):
    now = datetime.datetime.now()
    until_time = now + datetime.timedelta(minutes=minutes)
    pause.until(until_time)

def toManyRequestSoRest(channel_id):
    user_response  = getCurrentUser()
    user_name = user_response['username']

    is_need_to_rest = True
    while is_need_to_rest:
        messages = getMessages(channel_id)
        arr = np.array(messages)
        messages = arr[0:6]

        is_need_to_rest = any(object['author']['username'] == user_name for object in messages)
        print("is_need_to_rest = {}".format(is_need_to_rest))
        if is_need_to_rest:
            print('too many request so need one minute rest')
            delay(1)

def checkIsInLastMessage(channel_id):
    user_response  = getCurrentUser()
    user_name = user_response['username']

    messages = getMessages(channel_id)
    # print(messages)
    arr = np.array(messages)
    messages = arr[0:14]

    return any(object['author']['username'] == user_name for object in messages)

if __name__ == "__main__":
    channel_id = init()
    print(channel_id)
    while True:
        need_delete = checkIsInLastMessage(channel_id)
        print(need_delete)
        if need_delete:
            print('need to delete')
            response = sendMessage(channel_id,'! rank')
            print("response_finish time = {}".format(datetime.datetime.now()))
            response_json = response.json()
            message_id = data = response_json['id']

            deleteMessage(channel_id,message_id)
            delay(1)
            print('delete finish')

            continue

        response = sendMessage(channel_id,'!rank')
        print("response_finish time = {}".format(datetime.datetime.now()))
        status_code  = response.status_code
        print("status_code time = {}".format(status_code))
        if status_code == 429 :
            data = response.json()
            retry_after = data['retry_after']
            retry_after = math.ceil(retry_after)
            print("retry_after = {}".format(retry_after))
            time.sleep(retry_after)
        else:
            delay(1)