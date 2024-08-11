import telebot
from telebot import apihelper
import os
import json
import logging
from datetime import datetime
from telebot.types import ReplyKeyboardMarkup,KeyboardButton

c = datetime.now()

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


apihelper.ENABLE_MIDDLEWARE = True

API_TOKEN =os.environ.get('API_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)




# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.info('triggerd welcome')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Help'),KeyboardButton('About'))
    bot.send_message(message.chat.id,'Hi welcome to bot',reply_markup=markup)

@bot.message_handler(func= lambda message:message.text=='About')
def send_about(message):
    about=message.text
    bot.send_message(message.chat.id,'This is a bot for test ')

@bot.message_handler(func=lambda message:message.text=='Help')
def help(message):
    helpp=message.text
    bot.send_message(message.chat.id,'whats wrog for you?')



bot.infinity_polling()
