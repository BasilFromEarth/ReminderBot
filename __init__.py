from flask import Flask
from telegram import telegram

app = Flask(__name__)

# telegram - api for telegram app-hook
app.register_blueprint(telegram)

if __name__ == "__main__":
    app.run()