from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.telegram import telegram
    app.register_blueprint(telegram)

    return app