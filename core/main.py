import telebot
from telebot import apihelper
import os
import json
from datetime import datetime


c = datetime.now()


apihelper.ENABLE_MIDDLEWARE = True

API_TOKEN =os.environ.get('API_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am pybot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.middleware_handler(update_types=['message'])
def modify_message(bot_instance, message):
    # modifying the message before it reaches any other handler 
    message.another_text = message.text + ':changed'
    


@bot.message_handler(func=lambda message : True)
def handle_text_doc(message):
    print(message.another_text,c)
	# bot.reply_to(message,message.another_text)
    
    
     


# @bot.message_handler(content_types=['document', 'audio' ])
# def handel_doc_aud(message):
#       if message.content_type == 'document':
#             bot.reply_to(message,'doc')
#       elif message.content_type == 'audio':
#             bot.reply_to(message,'audio')
# @bot.message_handler(regexp="amin")
# def handle_message(message):
# 	print('sayed hi')




bot.infinity_polling()
