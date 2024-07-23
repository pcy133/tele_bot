import telebot

# 替换为你的机器人 TOKEN
TOKEN = '7163080666:AAFNETst95bbshxfhbNxTF0jMRvNpqruySE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot is running...")
bot.polling()
