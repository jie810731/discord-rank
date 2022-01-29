import utility

def speakWord():
    speakWord = utility.getEnv('Message')

    if not speakWord:
        speakWord = '.'
    
    return speakWord

if __name__ == "__main__":
    token = utility.getEnv('Token')
    channel_id = utility.getEnv('Channel_Id')

    if token == None or channel_id == None :
        print('miss env')
        quit()

    speak_word = speakWord()

    while True:
        send_response = utility.sendMessage(token,channel_id,speak_word)
        response_json = send_response.json()
        message_id = response_json['id']

        utility.deleteMessage(token,channel_id,message_id)

        throttlingLimitsTimes = utility.throttlingLimitsTimes(send_response)

        if throttlingLimitsTimes < 60:
            utility.delay(0,1,0)
        else:
            utility.delay(throttlingLimitsTimes,0,0)