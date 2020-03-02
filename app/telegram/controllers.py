from flask import request
from telebot.types import Update, ForceReply, KeyboardButton, ReplyKeyboardMarkup
from app.database.models import User, Reminder
from .states import Context

from . import bot, telegram


@telegram.route('/', methods=['POST'])
def telegram_web_hook():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


messages = {
    "start": "Hello! I am Remindy.\n"
             "I would like to remind you about anything important. What reminder do you want to crate?\n",
    "help": "..."
}


@bot.message_handler(commands=['start'])
def send_welcome(msg):
    keyboard = ReplyKeyboardMarkup()
    button1 = KeyboardButton("Regular")
    #button2 = KeyboardButton("Once")
    keyboard.add(button1)
    bot.send_message(msg.chat.id, messages["start"], reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_help(msg):
    bot.send_message(msg.chat.id, messages["help"])


@bot.message_handler(regexp="Once")
def test_callback(msg):
    bot.send_message(msg.chat.id, "What should I remind you?")


@bot.message_handler(regexp="Regular")
def test_callback(msg):
    bot.send_message(msg.chat.id, "What should I remind you?")


@bot.message_handler(func=lambda msg: True, content_types=['text'])
def text_handler(msg):
    user = User.query.filter_by(tg_id=msg.from_user.id)
    print(msg)
    if not user:
        send_welcome(msg)

    user_state = Context(user.tg_id, user.state)
    user_state.text_request(msg)




"""
@bot.message_handler(func=lambda msg: True, content_types=['text'])
def  test_callback(call):
    reminders.append(call.text)
"""