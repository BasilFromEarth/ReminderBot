import telebot
import time

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


bot_token = "953344597:AAHDbeo6Qc9R8GEsoYCUU1BpkVBp0SqACAQ"
messages = {
    "start": "Hello! My name is Remindy.\n"
             "I am here to remind you about important stuff. What would you like me to remind you about?\n",
    "help": "Fuck yourself"
}

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, messages["start"])


@bot.message_handler(commands=['help'])
def send_weclome(message):
    bot.send_message(message.chat.id, messages["help"])

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    send_welcome(message)

@bot.callback_query_handler(func=lambda call: True)
def  test_callback(call):
    print(call)
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    number = call.data

    bot.delete_message(call.message.chat.id, call.message.message_id)

    bot.send_message(user_id, "Dear "+user_name+"\nCall "+number)
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
    while True:
        try:
            bot.polling()
        except:
            time.sleep(3)