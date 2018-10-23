from flask import Flask, request
import random
import os
from LUIS import *
from data import *
from old import *
from imp import *
from pymessenger.bot import Bot
from datetime import date
from datetime import time
from datetime import datetime







app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET','POST'])
def recieve_message():
    if request.method =='GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    print (message)
                    response_sent_text = get_message(message['message']['text'])
                    send_message(recipient_id, response_sent_text)
                
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message("")
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"
    

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"


def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

if __name__ == '__main__':
    app.run()
