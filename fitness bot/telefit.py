from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram import *
import requests
import re

def start(bot, update):
    chat_id = update.message.chat_id
    msg_id = update.message.message_id
    bot.sendMessage(chat_id=chat_id, text="Hi i am BOBO😃. Your fitness bot🏋\nAre you ready to work out\n/yes\n/no,I am just here for health tip\nTo start a conversation next time type'/hi'", reply_to_message_id=msg_id)

def hi(bot, update):
    chat_id = update.message.chat_id
    msg_id = update.message.message_id
    bot.sendMessage(chat_id=chat_id, text="Hi i am BOBO😃. Your fitness bot🏋\nAre you ready to work out\n/yes\n/no,I am just here for health tip\nTo start a conversation next time type'/hi'", reply_to_message_id=msg_id)
def yes(bot, update):
    chat_id = update.message.chat_id
    msg_id = update.message.message_id
    bot.sendMessage(chat_id=chat_id, text="Good choice😊. What part of the body do you want to work on:\n/Upper_body(CHEST&ARM)\n/ABS(STOMACH)\n/Legs\n/Full_body_workout", reply_to_message_id=msg_id)

def fullbody(bot, update):
    chat_id = update.message.chat_id
    msg_id = update.message.message_id
    bot.sendMessage(chat_id=chat_id, text="Day 1 - 20 mins leg https://youtu.be/GfUpbhaCK7Y\nDay 2 - 5 chest 5 arm https://youtu.be/_q_-adYzkh0 \nDay 3 - 20 min cardio, 5 back https://youtu.be/c8IqjLwcN-c\nDay 4 - 20 mins morning, 5 shoulder https://youtu.be/yF4B0OPAOJY \nDay 5 - full body workout https://youtu.be/oAPCPjnU1wA", reply_to_message_id=msg_id)



def main():
    updater = Updater('1246861614:AAEW0WF8ZTPxbx-EAwVyBYYmlVPLqcxCGrs')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('hi',hi))
    dp.add_handler(CommandHandler('yes',yes))
    dp.add_handler(CommandHandler('full_body_workout',fullbody))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()