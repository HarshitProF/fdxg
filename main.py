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
        data={
            'dat':jsot[0],
            'pair':jost[2].split(":")[1],
            'type':jost[3],
            'leverage':jost[4].split(":")[1],
            'entery':jost[5].split(":")[1],
            'target':[jost[7].split(":")[1],jost[8].split(":")[1],jost[9].split(":")[1],jost[10].split(":")[1],jost[11].split(":")[1],jost[12].split(":")[1],jost[13].split(":")[1]]
            'stoploss':jost[15].split(":")[1]
        }
        print(data)
        return ''
if __name__=='__main__':
    app.run()
