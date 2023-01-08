from flask import Flask,url_for,request
from telebot import TeleBot
from telebot.types import Update
import requests
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
        chat_id=json.loads(json_string)['message']['from']['id']
        data={
            'dat':jsot[0],
            'pair':jsot[2].split(":")[1],
            'type':jsot[3],
            'leverage':jsot[4].split(":")[1],
            'entry':jsot[5].split(":")[1],
            'targets':[float(jsot[7].split(":")[1]),float(jsot[8].split(":")[1]),float(jsot[9].split(":")[1]),float(jsot[10].split(":")[1]),float(jsot[11].split(":")[1]),float(jsot[12].split(":")[1]),float(jsot[13].split(":")[1])],
            'stoploss':jsot[15].split(":")[1]
        }
        message1=f"✨{data['pair']}\n\n🎗 Trade Type={data['type']}\n\n💫 Leverage={data['leverage']}\n\n⚡️ Entry={data['entry']}\n\n❌ StopLoss={data['stoploss']}\n\n❎ Take profit={data['targets']}"
        url=f"https://api.telegram.org/bot{apikey}/sendMessage?chat_id={chat_id}&text={message1}"
        result=requests.get(url)
        print(result.text)
        return ''
if __name__=='__main__':
    app.run()
