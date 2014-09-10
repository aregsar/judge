from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.uuid import FlaskUUID

db = SQLAlchemy()
flaskuuid = FlaskUUID()

def init_plugins(app):
    db.init_app(app)
    flaskuuid.init_app(app)



