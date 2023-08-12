from flask import Flask
from flask_bcrypt import Bcrypt
from config import app

bcrypt = Bcrypt(app)
secret_key = app.config["SECRET_KEY"]
