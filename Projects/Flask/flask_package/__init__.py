from flask import Flask
from logging import DEBUG
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#hardcoding key is okay in dev but in prod need to store it in a protected file and input it to flask app
app.secret_key = b'w\xbeR>\xf0\x8epN'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.logger.setLevel(DEBUG)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flask_package import routes