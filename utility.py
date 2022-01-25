import os
import requests
import datetime
import pause 
import json

EMOJI_CELEBRATE = "%F0%9F%8E%89"

def delay(seconds=0,minutes=0,hours=0):
    now = datetime.datetime.now()
    print("now is = {}".format(now))
    until_time = now + datetime.timedelta(hours=hours,minutes=minutes,seconds=seconds)
    print("delay to = {}".format(until_time))
    pause.until(until_time)

def getEnv(key):
    try:
        value = os.environ[key]
    except Exception as e:
        print('does not pass env key = {}'.format(key))
        value = None
    
    return value

def getCurrentUser(token):
    url = "https://discord.com/api/v9/users/@me"
    
    header = {
            "Authorization": token,
            "Content-Type": "application/json",
    }

    res = requests.get(url=url, headers=header)
    data = res.json()

    return data

def getMessages(token,channel_id):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)

    header = {
            "Authorization": token,
            "Content-Type": "application/json",
    }

    res = requests.get(url=url, headers=header)
    data = res.json()

    return data 

def sendMessage(token,channel_id,message):
    msg = {
            "content": message
    }
    
    header = {
            "Authorization": token,
            "Content-Type": "application/json",
    }

    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
 
    res = requests.post(url=url, headers=header, data=json.dumps(msg))

    return res

def deleteMessage(token,channel_id,message_id): 
    url = "https://discord.com/api/v9/channels/{}/messages/{}".format(channel_id,message_id)

    header = {
            "Authorization": token,
            "Content-Type": "application/json",
    }

    res = requests.delete(url=url, headers=header)


def sendReaction(token,channel_id,message_id,reaction):
    url = "https://discord.com/api/v9/channels/{}/messages/{}/reactions/{}/@me".format(channel_id,message_id,reaction)
    header = {
            "Authorization": token,
            "Content-Type": "application/json",
    }

    res = requests.put(url=url, headers=header)

def throttlingLimitsTimes(sendResponse):
    status_code = sendResponse.status_code
    if status_code == 429 :
        data = response.json()
        retry_after = data['retry_after']
        retry_after = math.ceil(retry_after)

        return retry_after
    
    return 0

def getUsers():
    url = "https://api.npoint.io/598faaae1ce7ed2de7ea"

    res = requests.get(url=url)
    data = res.json()

    return data 
