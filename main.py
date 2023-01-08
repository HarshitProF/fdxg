from flask import Flask,url_for,request
from telebot import TeleBot
from telebot.types import Update
app=Flask(__name__)
apikey='5820722020:AAE04TjGoFouhLZ54MDMpssc3j46HhINAqw'
bot=TeleBot(apikey)
@bot.message_handler(func=lambda message:True)
def send(message):
    print(message)
    bot.reply_to(message,text="hello")
@app.route('/')
def setweb():
    url=url_for(setweb)+apikey
    bot.remove_webhook(url)
    return  bot.remove_webhook(url)
@app.route(url_for(setweb)+apikey,methods=['POST'])
def send2():
    if request.method=='POST':
        json_string=request.get_data().decode('utf-8')
        update=Update.de_json(json_string)
        bot.process_new_updates([update])
if __name__=='__main__':
    app.run()