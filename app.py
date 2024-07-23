from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 处理 /start 命令
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('你好！我是一个回声机器人。你发什么我就回什么。')

# 处理回声消息
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# 处理错误
def error(update: Update, context: CallbackContext) -> None:
    print(f'Update {update} caused error {context.error}')

def main():
    # 在这里替换为你的 Telegram 机器人 Token
    token = 'Y7163080666:AAFNETst95bbshxfhbNxTF0jMRvNpqruySE'

    # 创建 Updater 对象
    updater = Updater(token)

    # 获取调度器
    dispatcher = updater.dispatcher

    # 添加命令处理程序
    dispatcher.add_handler(CommandHandler("start", start))

    # 添加消息处理程序
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 添加错误处理程序
    dispatcher.add_error_handler(error)

    # 启动机器人
    updater.start_polling()

    # 保持机器人运行
    updater.idle()

if __name__ == '__main__':
    main()
