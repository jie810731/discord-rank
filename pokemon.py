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

    header['Authorization'] = token

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

def delay(minutes):
        now = datetime.datetime.now()
        until_time = now + datetime.timedelta(minutes=minutes)
        pause.until(until_time)

def getMessages(channel): 
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel)
    try:
        res = requests.get(url=url, headers=header)

        data = res.json()
    except:
        pass
    return data


def battle():
    now = datetime.datetime.now()
    until_time = now + datetime.timedelta(minutes=1)
    
    sendMessage(927963670330351686,'.route 1')
    time.sleep(5)
    # sendMessage(927963670330351686,'1')
    message = getMessages(927963670330351686)

    keep_attect = True

    while keep_attect:
        attect_method = random.choice(["1", '2'])
        sendMessage(927963670330351686,attect_method)
        time.sleep(5)
        messages = getMessages(927963670330351686)
        for message in messages:
            name = ''
            if  len(message['embeds']) > 0:     
                try:
                    name = message['embeds'][0]['author']['name']
                except KeyError:
                    # Key is not present
                    pass
            if name.find('Charmander') != -1:
                break  

            if  name == 'Wild battle has ended!':
                keep_attect = False
                print('battle ended')

                break

            if  name == "Trainer's Linebacker battle ended!":
                keep_attect = False
                print('battle ended')

                break 

            if  name.find('ended!') != -1:
                keep_attect = False
                print('battle ended')

                break 

            if  name.find('Swapping') != -1:
                sendMessage(927963670330351686,'Rattata')

                break

    now = datetime.datetime.now()
    print(now)
    print(until_time)
    if now < until_time:
        print('need delay')
        pause.until(until_time)
        print('delay finish')
             

if __name__ == "__main__":
    init()
    while True:
        battle()