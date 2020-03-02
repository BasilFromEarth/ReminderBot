import os
import logging

from flask import Flask
from .database.models import db

def configure_logging():
    # register root logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.INFO)


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv("APP_SETTINGS", 'config.DevConfig'))
    configure_logging()

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.telegram import telegram
    app.register_blueprint(telegram)

    return app
