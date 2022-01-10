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

def init():
    token = os.environ['Token']
    # token ='OTIwOTUwMTE3MjI4NDkwNzky.YdwHIQ.pzXeESYrlZkS7bjPPQ_ry4HZi5w'
    if not token:
        raise Exception('empty token')

    header['Authorization'] = token

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

def eagleSendMessage(channel_1_id,channel_2_id):
    channel_1_message_response = getMessages(channel_1_id)
    last_message = channel_1_message_response[-1]

    sendMessage(channel_2_id,last_message['content'])
    # channel_2_message_response = getMessages(channel_2_id)
    # arr = np.array(channel_2_message_response)
    # channel_2_message_response = arr[0:10]

    # if any(object['content'] != last_message['content'] for object in channel_2_message_response) :
    #     sendMessage(channel_2_id,last_message['content'])

def changeSort(channels):
    return [channels[1],channels[0]]

def delay(minutes):
        now = datetime.datetime.now()
        until_time = now + datetime.timedelta(minutes=minutes)
        pause.until(until_time)

def minutesAfter(minutes):
    now = datetime.datetime.now()
    until_time = now + datetime.timedelta(minutes=minutes)

    return until_time

if __name__ == "__main__":
    init()
    channels = [927892453074276412,927857490488606720]  
    new_time = minutesAfter(10)
    while True:
        eagleSendMessage(channels[0],channels[1])
        channels = changeSort(channels)
        delay(1)
        now = datetime.datetime.now()
        if now > new_time:
            delay(10)
            new_time = minutesAfter(10)
