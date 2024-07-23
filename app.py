import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get('7163080666:AAFNETst95bbshxfhbNxTF0jMRvNpqruySE')
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://cy1sryan-8e7ebb2bd5bf.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
