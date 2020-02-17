from flask import request
from telebot.types import Update, ForceReply, KeyboardButton, ReplyKeyboardMarkup
from app.database.models import db, Users, Reminders

from . import bot, telegram


@telegram.route('/', methods=['POST'])
def telegram_web_hook():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


messages = {
    "start": "Hello! I am Remindy.\n"
             "I would like to remind you about anything important. What would you like me to remind you about?\n",
    "help": "..."
}


@bot.message_handler(commands=['start'])
def send_welcome(msg):
    keyboard = ReplyKeyboardMarkup()
    button1 = KeyboardButton("Regularly")
    button2 = KeyboardButton("Once")
    keyboard.add(button1, button2)
    bot.send_message(msg.chat.id, messages["start"], reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_help(msg):
    bot.send_message(msg.chat.id, messages["help"])


@bot.message_handler(regexp="Once")
def test_callback(msg):
    bot.send_message(msg.chat.id, "What should I remind you?")



"""
@bot.message_handler(func=lambda msg: True, content_types=['text'])
def  test_callback(call):
    reminders.append(call.text)
"""