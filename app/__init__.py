import os

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'
from app import routes, models

