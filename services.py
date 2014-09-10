from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.uuid import FlaskUUID

db = SQLAlchemy()
flaskuuid = FlaskUUID()

def initialize_services(app):
    db.init_app(app)
    flaskuuid.init_app(app)



