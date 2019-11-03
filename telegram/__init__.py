import os
import telebot
from flask import Blueprint

telegram = Blueprint("telegram", __name__)
bot = telebot.TeleBot(token="953344597:AAHDbeo6Qc9R8GEsoYCUU1BpkVBp0SqACAQ")

from . import cotrollers