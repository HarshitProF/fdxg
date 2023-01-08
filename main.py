from flask import Flask,url_for,request
from telebot import TeleBot
from telebot.types import Update
import json
app=Flask(__name__)
apikey='5820722020:AAE04TjGoFouhLZ54MDMpssc3j46HhINAqw'
@app.route(f'/'+apikey,methods=['POST'])
def send2():
    if request.method=='POST':
        json_string=request.get_data().decode('utf-8')
        print(json_string)
        update=Update.de_json(json_string)
        jsot=json.loads(json_string)['message']['text'].split('\n')
        print(jsot)
        return ''
if __name__=='__main__':
    app.run()
