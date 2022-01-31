import utility

def getTokens():
    user_objects = utility.getUsers()
    garbleds = []

    for object in user_objects['object']:
        user_response = utility.getCurrentUserResponse(object['garbled'])

        if user_response.status_code == 401:
            notify_message = '{} token is invalidate'.format(object['name'])
            utility.notify(notify_message)
            continue
    
        garbleds.append(object['garbled'])
    
    return garbleds

def getChannels():
    user_objects = utility.getUsers()
    
    return user_objects['channal_id']


if __name__ == "__main__":
    while True:
        channels = getChannels()
        tokens = getTokens()
        
        for token in tokens:
            for channel in channels:
                channel_id = channel['channel_id']
                messages = utility.getMessages(token,channel_id)

                if type(messages) is dict:
                    continue
                    
                for message in messages:
                    content = message['content']

                    if content.find('GIVEAWAY') != -1:
                        message_id = message['id']
                        utility.sendReaction(token,channel_id,message_id,utility.EMOJI_CELEBRATE)

        utility.delay(0,14,0)