from telegram.ext import Updater, CommandHandler
import requests

TOKEN = '7782948865:AAHfjOXAbXjs3C6-EjRyc7yWSVQvIWtO0D8'

def start(update, context):
    context.bot.send_message(chat_id=(link unavailable), text='Welcome to Website Tester Bot!')

def test_website(update, context):
    url = context.args[0]
    # Add testing logic here
    context.bot.send_message(chat_id=(link unavailable), text=f'Testing {url}...')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('test', test_website))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
