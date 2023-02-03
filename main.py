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
        try:
            jsot=json.loads(json_string)['message']['text'].split('\n')
        except :
            jsot=json.loads(json_string)['edited_message']['text'].split('\n')
        try:
            chat_id=json.loads(json_string)['message']['from']['id']
        except:
            chat_id=json.loads(json_string)['edited_message']['from']['id']
        print(jsot)
        data={
            'dat':jsot[0],
            'pair':jsot[2].split(":")[1],
            'type':jsot[3],
            'leverage':jsot[4].split(":")[1],
            'entry':jsot[5].split(":")[1],
            'targets':[float(jsot[7].split(":")[1]),float(jsot[8].split(":")[1]),float(jsot[9].split(":")[1]),float(jsot[10].split(":")[1]),float(jsot[11].split(":")[1]),float(jsot[12].split(":")[1]),float(jsot[13].split(":")[1])],
            'stoploss':jsot[15].split(":")[1]
        }
        pairs=data['pair'][[0:len(data['pair'])-4]
        print(pairs)
        message1=f"✨{data['pair']}\n\n🎗 Trade Type={data['type']}\n\n💫 Leverage={data['leverage']}\n\n⚡️ Entry={data['entry']}\n\n❌ StopLoss={data['stoploss']}\n\n❎ Take profit={data['targets']}"
        message2=f"📍 {data['pair']}\n\n🏹 Signal Type:- {data['type']}\n\n💫Leverage: {data['leverage']}\n\n👉 Entry Targets:- {data['entry']}\n\n🎯 Profit Targets:\n1) {data['targets'][0]}\n2) {data['targets'][1]}\n3) {data['targets'][2]}\n4) {data['targets'][3]}\n5) {data['targets'][4]}\n6) {data['targets'][5]}\n7) {data['targets'][6]}\n\n🛑 Stop Target: {data['stoploss']} "
        message3=f"⚡️💫 {data['pair']} 💫⚡️\n\n[{data['type']}]:{data['entry']}\n\n✨🎯 TARGETS ✨🎯\n\n1.Goal👉 {data['targets'][0]}\n2.Goal👉 {data['targets'][1]}\n3.Goal👉 {data['targets'][2]}\n4.Goal👉 {data['targets'][3]}\n5.Goal👉 {data['targets'][4]}\n6.Goal👉 {data['targets'][5]}\n7.Goal👉 {data['targets'][6]}\n\nSL🛑:- {data['stoploss']}\n\n🎗 LEVERAGE:- {data['leverage']}"
        messages=[message1,message2,message3]
        for message in messages:
            url=f"https://api.telegram.org/bot{apikey}/sendMessage?chat_id={chat_id}&text={message}"
            result=requests.get(url)
            print(result.text)

        return ''
if __name__=='__main__':
    app.run()
