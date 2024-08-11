import telebot
from telebot import apihelper
import os
import json
import logging
from datetime import datetime
from telebot import types

c = datetime.now()

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


apihelper.ENABLE_MIDDLEWARE = True

API_TOKEN =os.environ.get('API_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)




# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    logger.info('triggerd welcome')
    bot.reply_to(message, """\
Hi there, I am pybot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['setname'])
def assignment(message):
    bot.send_message(message.chat.id,'Hi whats your name?')
    bot.register_next_step_handler(message,firstname)


def firstname(message,*args,**kwargs):
    name =message.text
    bot.send_message(message.chat.id,'Good!! tell me your last name')
    bot.register_next_step_handler(message,lastnamee,name)

def lastnamee(message,name):
    lastname = message.text
    bot.send_message(message.chat.id,f'welcome {name} {lastname} tell me your age')
    bot.register_next_step_handler(message,age,lastname,name)

def age(message,lastname,name):
    agee = message.text
    bot.send_message(message.chat.id,f'your name is {name} \n your lastname is {lastname} \n and your age is {agee}')



bot.infinity_polling()
