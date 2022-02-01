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
                    
                for message in messages[0:5]:
                    content = message['content']
                    content = content.upper()

                    embed = ''
                    embeds = message['embeds']
                    if len(embeds) > 0:
                        try:
                            embed = embeds[0]['title'] 
                            embed = embed.upper()
                        except:
                            pass
                    if content.find('GIVEAWAY') != -1 or embed.find('GIVEAWAY') != -1:
                        try:
                            reactions = message['reactions']
                            reaction = next((x for x in reactions if x['emoji']['name'] == '🎉'), None)
                            if reaction :
                                is_click = reaction['me']
                                if is_click == True:
                                    continue
                        except Exception as e:
                            pass
                        
                        message_id = message['id']
                        print('channel_id = {} message id = {} token = {} send emoji'.format(channel_id,message_id,token))
                        utility.sendReaction(token,channel_id,message_id,utility.EMOJI_CELEBRATE)
                        utility.delay(1,0,0)

        utility.delay(0,14,0)