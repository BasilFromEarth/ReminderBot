import os
import telebot
import logging
from flask import Blueprint

telegram = Blueprint("telegram", __name__)
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
logging.info(bot.set_webhook(os.getenv('HOOK_URL')))

from . import controllers
