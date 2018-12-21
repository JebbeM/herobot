import os
from datetime import time
import configparser
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = None
chat_id = None

try:
    #If running on herkou
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
except:
    #If running locally
    config = configparser.ConfigParser()
    config.read('config.txt')
    token = config['LOCAL']['token']
    chat_id = config['LOCAL']['chat_id']

updater = Updater(token=token)
dispatcher = updater.dispatcher
queue = updater.job_queue

####################################
# Example bot command

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Started!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

####################################
# Example of a daily remainder message sent to one channel

def send_daily(bot, job):
    msg = bot.send_message(chat_id=chat_id, text="This message is sent every day!")

job_daily = queue.run_daily(send_daily,time=datetime.time(hour=12, minute=0))

####################################
print("Starting polling")
updater.start_polling()
