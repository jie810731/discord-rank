import utility

if __name__ == "__main__":
    while True:
        token = utility.getEnv('Token')
        channel_id = utility.getEnv('Channel_Id')

        if token == None or channel_id == None :
            print('miss env')
            quit()

        messages = utility.getMessages(token,channel_id)

        for message in messages:
            content = message['content']

            if content.find('**GIVEAWAY**') != -1:
                message_id = message['id']
                utility.sendReaction(token,channel_id,message_id,utility.EMOJI_CELEBRATE)

        utility.delay(0,0,1)