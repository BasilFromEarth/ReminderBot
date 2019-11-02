import telebot
import time

from flask import request, Flask
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, Update

bot_token = "953344597:AAHDbeo6Qc9R8GEsoYCUU1BpkVBp0SqACAQ"
messages = {
    "start": "Hello! My name is Remindy.\n"
             "I am here to remind you about important stuff. What would you like me to remind you about?\n",
    "help": "Fuck yourself"
}

bot = telebot.TeleBot(token=bot_token)
app = Flask(__name__)

reminders = []
chat_id = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, messages["start"], reply_markup=ForceReply())


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, messages["help"])


@bot.message_handler(func=lambda msg: True, content_types=['text'])
def  test_callback(call):
    reminders.append(call.text)


@app.route('/', methods=['POST'])
def telegram_web_hook():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200
"""
def send_message(id, chatID):
    order = Order.query.all()
    number = str(Order.query.get(id))

    reply = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Accept', callback_data=number)
    reply.add(button)

    bot.send_message(chatID, "Destroy manager!", reply_markup=reply)
"""
if __name__ == "__main__":
    app.run()
    if time.localtime().tm_sec == 0:
        bot.send_message(chat_id, reminders[0])
