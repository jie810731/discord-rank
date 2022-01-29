import requests
import json
import datetime
import pause
import time
import math
import numpy as np
import os
import random

header = {
            "Authorization": "OTIwOTUwMTE3MjI4NDkwNzky.YdTofw.3dot1Af3IkNxt36P2RUOp0Hqcc4",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }


def init():
    token = os.environ['Token']
    if not token:
        raise Exception('empty token')
    channel_id = os.environ['Channel_Id']
    if not token:
        raise Exception('empty token')
    
    if not channel_id:
        raise Exception('empty channel id')


    header['Authorization'] = token

    return channel_id

def getMessages(channel): 
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel)
    try:
        res = requests.get(url=url, headers=header)

        data = res.json()
    except:
        pass
    return data

def sendMessage(channel_id,message): 
    msg = {
            "content": message
    }
    
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    try:
        res = requests.post(url=url, headers=header, data=json.dumps(msg))

    except:
        pass

    return res



if __name__ == "__main__":
    channel_id  = init()
    while True:
        messages = getMessages(channel_id)
        last_message = messages[-1]
        response = sendMessage(channel_id,last_message['content'])
        status_code  = response.status_code
        print("status_code time = {}".format(status_code))
        if status_code == 429 :
            data = response.json()
            retry_after = data['retry_after']
            retry_after = math.ceil(retry_after)
            print("retry_after = {}".format(retry_after))
            time.sleep(retry_after)
        else:
            time.sleep(random.randint(5,10))