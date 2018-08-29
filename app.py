from flask import Flask, request
import random
import os
from pymessenger.bot import Bot
from datetime import date
from datetime import time
from datetime import datetime





hello =['hi','hello','hii','hiii','aloha','hola']
bye=['bye', 'byebye','bye bye','ciao']
HAU=['how are you','how are you?']
time=['time','what is the time','time?']
date=['what is the date','date','date?','date ?']
RPS=['rock','paper','scissor']
info=['info','information','?']
TOSS=['Heads','Tails']
toss=['toss','do a toss']
menu_m=['monday','monday menu']
menu_t=['tuesday','tuesday menu']
menu_w=['wednesday','wednesday menu']
menu_th=['thursday','thursday menu']
menu_f=['friday','friday menu']
menu_s=['saturday','saturday menu']
menu_sun=['sunday','sunday menu']


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



def get_message(inp):

    """
    print (message['nlp']['entities']['greetings'][0]['confidence'])
    x1,x2,x3='','',''
    if message['nlp']['entities']['greetings'][0]['confidence']> 0.98:
        x1="Hello :)"
     
    if message['nlp']['entities']['thanks'][0]['confidence']> 0.98:
        x2="Your Welcome"
    if message['nlp']['entities']['bye'][0]['confidence']> 0.98:
        x3="Bye"
        
    sample= ['1','2','3']
    ran=random.choice(sample)
    xn=x1+x2+x3
    """

    a,e='',''
    for y1 in hello:
        if inp.lower()==y1:
            a="Hello! :) \nTry Rock paper scisors \nAsk the date or time\nSay toss to flip a coin"
            break
    for y2 in bye:
        if inp.lower()==y2:
            a="Bye"
            break
    for y3 in HAU:
        if inp.lower()==y3:
            a="I'm fine, What about you?"
            break
    for y4 in time:
        if inp.lower()==y4:
            
            k=str(datetime.time(datetime.now()))
            a="The time is "+k
            break
    for y5 in date:
        if inp.lower()==y5:
            k=str(datetime.date(datetime.now()))
            a="The date is "+k
            break
    for y6 in RPS:
        if inp.lower()==y6:
            bm=random.choice(RPS)
            a=bm
            if (((inp.lower()=='rock')and bm=='scissor')or(inp.lower()=='paper'and bm=='rock')or (inp.lower()=='scissor'and bm=='paper')):
                a=bm+','+"You win"
            elif inp.lower()==bm:
                a=bm+','+"It's a tie!"
            else:
                a=bm+','+ "I win"
            break

    for y6 in toss:
        if inp.lower()==y6:
            bm=random.choice(TOSS)
            a=bm
            break
        for y in info:
            if inp.lower()==y:
                a="Chat Bot Test is an expertimental chat bot deployed on Facebook Messenger by Siddhant Saoji \nThis bot is currently in devlpoment phase"
                break
                
    for d in menu_m:
        if inp.lower()==d:
            a="(Breakfast)Poha Jalebi|| (Lunch)||Plain Rice, Arhar dal, Lauki Chana,Boondi Raita||(Dinner) Jeera Rice, Moong-Masoor Dal,Chhole Bhature"
            break
    for d in menu_t:
        if inp.lower()==d:
            a="(Breakfast)Uttpam, Sambhar, Coconut Chutney|| (Lunch)||Plain Rice, Dal Tadka, Aloo Matar,Seasonal Fruit Papaya||(Dinner) Fried Rice, Dal Tadka,Manchurian Gravy"
            break
    for d in menu_w:
        if inp.lower()==d:
            a="(Breakfast)Pyaaz and Azwain Paratha, Aloo Sabji|| (Lunch)||Plain Rice, Arhar dal, Lauki Chana,Boondi Raita,Chhachh||(Dinner) Plain Rice, Arhar Dal,Mix Veg"
            break     
    for d in menu_th:
        if inp.lower()==d:
            a="(Breakfast)Idli / Fried Idli, Sambhar, Coconut Chutney|| (Lunch)||Plain Rice, Yellow Arhar-Moong dal,Kadhi-Pakoda, Black Chana||(Dinner)Plain Rice, Arhar Dal, Red Pumpkin,Gulab Jamun/ Kala Jamun"
            break
    for d in menu_f:
        if inp.lower()==d:
            a="(Breakfast)Poori Sabji|| (Lunch)||Lemon Rice, Chana Dal, Bhindi Aloo,Banana,Gauva||(Dinner) Plain Rice, Dal Tadka,Paneer / Egg Curry, Ice Cream Cup#"
            break
    for d in menu_s:
        if inp.lower()==d:
            a="(Breakfast) Aloo Paratha, Dahi, Sauce, Pickle|| (Lunch) Fried Rice, Urad Dal,Veg Kolhapuri||(Dinner) Plain Rice, Dal Fry,Baingan Bharta, Boondi Laddu"
            break  
    for d in menu_sun:
        if inp.lower()==d:
            a="(Breakfast) Masala Dosa, Sambhar, Chutney|| (Lunch)Veg Biryani, Dal Fry, Paalak Aloo,||(Dinner) |Plain Rice, Dal Makhani,Cucumber Raita Paneer / Chicken, Rice Kheer"
            break  
 
            
    if a=='':
        e="Sorry this is not supported yet"
    ans= a+e
    print (ans)
    return ans

if __name__ == '__main__':
    app.run()
