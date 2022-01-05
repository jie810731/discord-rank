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

chanel_id = 917959442253893664

def init():

    token = os.environ['Token']
    channel_id = os.environ['Channel_Id']

    if not token:
        raise Exception('empty token')
    
    if not channel_id:
        raise Exception('empty channel id')


    header['Authorization'] = token
    chanel_id = channel_id

def sendMessage(): 
    msg = {
            "content": "!rank"
    }
    
    url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
    try:
        res = requests.post(url=url, headers=header, data=json.dumps(msg))

    except:
        pass

    return res

def deleteMessage(message_id): 
    
    url = "https://discord.com/api/v9/channels/{}/messages/{}".format(chanel_id,message_id)
    try:
        res = requests.delete(url=url, headers=header)

    except:

        pass

    return message_id

def getMessages(): 
    url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
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

def toManyRequestSoRest():
    user_response  = getCurrentUser()
    user_name = user_response['username']

    is_need_to_rest = True
    while is_need_to_rest:
        messages = getMessages()
        arr = np.array(messages)
        messages = arr[0:4]

        is_need_to_rest = any(object['author']['username'] == user_name for object in messages)
        print("is_need_to_rest = {}".format(is_need_to_rest))
        if is_need_to_rest:
            print('too many request so need one minute rest')
            delay(1)

# def oauth2Me():
#     API_ENDPOINT = 'https://discord.com/api/v8'
#     CLIENT_ID = '928125812077637642'
#     CLIENT_SECRET = 'yh572vVZbUgVNbNVmAc7URNn-sOgaREj'


#     data = {
#         'grant_type': 'client_credentials',
#         'scope': 'identify applications.commands.update rpc'
#     }
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
#     r.raise_for_status()

#     r_json = r.json()

#     return r_json['access_token']
    

if __name__ == "__main__":
    # test = oauth2Me()
    # header['Authorization'] = "Bearer {}".format(test)
    # print(header)

    init()
    while True:
        toManyRequestSoRest()
        response = sendMessage()
        print("response_finish time = {}".format(datetime.datetime.now()))
        status_code  = response.status_code
        print("status_code time = {}".format(status_code))
        if status_code == 429 :
            data = response.json()
            retry_after = data['retry_after']
            retry_after = math.ceil(retry_after)
            print("retry_after = {}".format(retry_after))
            time.sleep(retry_after)

    
