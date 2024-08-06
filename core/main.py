import telebot
import os
import json

API_TOKEN =os.environ.get('API_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """\
# Hi there, I am pybot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)
    #   bot.send_message(message.chat.id,json.dumps(message.chat.__dict__,indent=4,ensure_ascii=False))
      # bot.reply_to(message,'hi there')

# @bot.message_handler(content_types=['document', 'audio' ])
# def handel_doc_aud(message):
#       if message.content_type == 'document':
#             bot.reply_to(message,'doc')
#       elif message.content_type == 'audio':
#             bot.reply_to(message,'audio')
# @bot.message_handler(regexp="amin")
# def handle_message(message):
# 	print('sayed hi')
@bot.message_handler(func=lambda message: message.text == 'Hi')
def handle_text_doc(message):
	print('lambda')



bot.infinity_polling()
