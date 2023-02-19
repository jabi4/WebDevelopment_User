from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.Config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

from endpoints.UserEndpoint import users
app.register_blueprint(users, url_prefix="/users")
