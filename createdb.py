from flask import Flask
from config import Config
from flask.ext.sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
print db
#create database judgedb using psql
#$ psql
#aregsarkissian=#createdb judgedb
#list all the databases
#regsarkissian=# \l
#recreate the database(does not drop the database)
db.drop_all()
db.create_all()
#work with the database
#$psql judgedb
#judgedb=# SELECT * FROM pg_catalog.pg_tables
