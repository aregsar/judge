from flask import Flask
from config import Config
from flask.ext.sqlalchemy import SQLAlchemy
import psycopg2
from models.user import User

app = Flask(__name__)
app.config.from_object(Config)
with app.app_context():
    # This should work because we are in an app context.
    db = SQLAlchemy()
    db.app=app
    db.init_app(app)
    print db
    #create database judgedb using psql
    #$ psql
    #aregsarkissian=#createdb judgedb
    #list all the databases
    #regsarkissian=# \l
    #recreate the database(does not drop the database)


    #db.drop_all()
    db.create_all()
    db.session.commit()
    user = User.query.filter_by(email="test").first()
    print user
#work with the database
#$psql judgedb
#judgedb=# SELECT * FROM pg_catalog.pg_tables
