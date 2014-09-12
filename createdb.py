from flask import Flask
from config import Config
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#recreate the database
db.drop_all
db.create_all
