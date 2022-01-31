import os
import requests
import datetime
import pause 
import json
import math
from dotenv import load_dotenv

load_dotenv()
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

def getCurrentUserResponse(token):
    url = "https://discord.com/api/v9/users/@me"
    
    header = {
            "Authorization": token,
            "Content-Type": "application/json",
    }

    res = requests.get(url=url, headers=header)

    return res

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
        data = sendResponse.json()
        retry_after = data['retry_after']
        retry_after = math.ceil(retry_after)

        return retry_after
    
    return 0

def getUsers():
    url = getEnv('USERS_API')
    res = requests.get(url=url)
    data = res.json()

    return data 

def notify(messages):
    body = {
        "chat_id" : -790427094,
        "text" : messages,
        "parse_mode" : "markdown"
    }

    url = 'https://api.telegram.org/bot5277878862:AAGh-AfBwn35qBomaV0OoH3B9bxDvWwYnDs/sendMessage'
    header = { 
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }   
    res = requests.get(url=url, headers=header,data=json.dumps(body))
    data = res.json()