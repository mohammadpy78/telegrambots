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
    markup= ReplyKeyboardMarkup(resize_keyboard=True,input_field_placeholder='Choose your option: ')
    markup.add(KeyboardButton(text='Help'),KeyboardButton(text='About'))
    markup.add(KeyboardButton('test1'),KeyboardButton('test2'))
    bot.send_message(message.chat.id,'this is test',reply_markup=markup)
@bot.message_handler(func= lambda message:message.text =='About')
def send_about(message):
    bot.send_message(message.chat.id,'this is bot for test')

@bot.message_handler(func= lambda message:message.text =='Help')
def send_about(message):
    bot.send_message(message.chat.id,'whats wrong for you?')

@bot.message_handler(func= lambda message:message.text=='test1')
def send_test1(message):
    bot.send_message(message.chat.id,'this is test1')

@bot.message_handler(func= lambda message:message.text=='test2')
def send_test2(message):
    bot.send_message(message.chat.id,'this is test2')




bot.infinity_polling()
