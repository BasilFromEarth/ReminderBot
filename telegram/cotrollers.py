from flask import request
from telebot.types import Update, ForceReply

from . import bot, telegram

@telegram.route('/', methods=['POST'])
def telegram_web_hook():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    print("12")
    return 'ok', 200

messages = {
    "start": "Hello! My name is Remindy.\n"
             "I am here to remind you about important stuff. What would you like me to remind you about?\n",
    "help": "Fuck yourself"
}
reminders = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("123")
    bot.send_message(message.chat.id, messages["start"], reply_markup=ForceReply())


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, messages["help"])


@bot.message_handler(func=lambda msg: True, content_types=['text'])
def  test_callback(call):
    reminders.append(call.text)
