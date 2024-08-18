import telebot
from telebot import apihelper
import os
import json
import logging
from datetime import datetime
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup

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
    markup = InlineKeyboardMarkup()
    button_google=InlineKeyboardButton(text='google',url='https://google.com')
    button_youtube=InlineKeyboardButton(text='YouTube',url='https://youtube.com')
    button_test=InlineKeyboardButton('test button',callback_data='test')
    markup.add(button_google,button_youtube)
    markup.add(button_test)
    bot.send_message(message.chat.id,text='clicked the links',reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def send_data(call):
    if call.data == 'test':
        logger.info('send data test')
        bot.answer_callback_query(call.id,text='clicked on button',show_alert=True)
        
   




bot.infinity_polling()
