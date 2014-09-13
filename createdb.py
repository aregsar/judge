from flask import Flask
from config import Config
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URL']='postgres://localhost/judgedb'
db = SQLAlchemy(app)
print db
#recreate the database
#db.drop_all()
#db.create_all()
