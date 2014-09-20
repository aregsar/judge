from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.uuid import FlaskUUID
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from flask.ext.moment import Moment
from flask import redirect,url_for

db = SQLAlchemy()
flaskuuid = FlaskUUID()
bcrypt = Bcrypt()
login_manager = LoginManager()
moment = Moment()

def init_plugins(app):
    db.init_app(app)
    flaskuuid.init_app(app)
    bcrypt.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    #login_manager.login_view =  "account.signin"



@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("home.index"))
