from app import db
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from datetime import datetime

class User(db.Model)
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),nullable=False, unique=True, index=True)
    barnumber = db.Column(db.String(255),nullable=False, unique=True, index=True)
    email = db.Column(db.String(255),nullable=False, unique=True, index=True)
    password = db.Column(db.String(2048),nullable=False)
    #user_role options: "member" or "mod" or "admin" or "sa"
    user_role = db.Column(db.String(50),nullable=False)
    signin_token = db.Column(db.String(255),nullable=True, unique=True, index=True)
    signedin_at = db.Column(db.DateTime,nullable=True)
    activated = db.Column(db.Boolean,nullable=False)
    activated_at = db.Column(db.DateTime,nullable=True)
    banned = db.Column(db.Boolean,nullable=False)

    #used to set the state of this object before passing it to flask logins login_user method
    authenticated = False


    def __init__(self,email,password,barnumber,username):
        self.password= set_password(password)
        self.email = email
        self.barnumber = barnumber
        self.username = username
        self.user_role = "member"
        self.activated = False
        self.banned = False

    def activate():
        self.activated = True
        self.activated_at = datetime.utcnow()

     def refresh_signin_token_and_date():
        self.signin_token = "areg"
        self.signedin_at = datetime.utcnow()

    def set_password(self):
        self.password= bcrypt.generate_password_hash(password))

    def is_banned(self):
        return self.banned

    def password_is_correct(self, password):
        return bcrypt.check_password_hash(self.password, password)



    #Flask-Login interface
    def get_id(self):
        return unicode(self.email)
        #return unicode(self.id)

    def is_active(self):
        return self.activated and not self.banned

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
    #end Flask-Login interface

    def __repr__(self):
        return '<email {}'.format(self.email)

#define after defining User
@login_manager.user_loader
def user_loader(user_id):
    #user_id is the value returned from User.get_id() method
    #it is first called by flask-login in the login_user(user) method
    #then this methode is called passing in the value returned rom User.get_id()
    #return User.query.get(user_id)
    return User.query.filter(User.email==user_id).first()

