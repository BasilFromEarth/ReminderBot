from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    tg_id = db.Column(db.Integer, nullable=False)
    lang = db.Column(db.String(3), nullable=False)


class Reminders(db.Model):
    __tablename__ = "Reminders"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    company_id = db.Column(db.Integer, nullable=False)
    name_company = db.Column(db.String(30), nullable=False)


