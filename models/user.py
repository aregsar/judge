from plugins import db, bcrypt,login_manager
#from flask.ext.login import LoginManager
from datetime import datetime

class User(db.Model):
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
    activation_token = db.Column(db.String(255),nullable=True, unique=True, index=True)
    activated_at = db.Column(db.DateTime,nullable=True)
    banned = db.Column(db.Boolean,nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)
    password_reset_token = db.Column(db.String(255),nullable=True, unique=True, index=True)

    #SecureRandom.urlsafe_base64

    #used to set the state of this object before passing it to flask logins login_user method
    authenticated = False

    def __init__(self,email,password,barnumber,username):
        self.username = username
        self.password= bcrypt.generate_password_hash(password)
        #self.password= self.set_password(password)
        self.email = email
        self.barnumber = barnumber
        self.user_role = "member"
        self.activated = False
        self.banned = False
        self.created_at = datetime.utcnow()
        self.signin_token = None
        self.signedin_at = None
        self.activation_token = None
        self.updated_at = None
        self.password_reset_token = None
        self.authenticated = False


    def set_password(self,password):
        self.password = bcrypt.generate_password_hash(password)

    def activate(self):
        dt = datetime.utcnow()
        self.activated = True
        self.activated_at = dt
        self.updated_at = dt

    def refresh_signin_token_and_date(self):
        dt = datetime.utcnow()
        self.signin_token = "areg"
        self.signedin_at = dt
        self.updated_at = dt

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
        return '<email {}>'.format(self.email)




#define after defining User
@login_manager.user_loader
def user_loader(user_id):
    #user_id is the value returned from User.get_id() method
    #it is first called by flask-login in the login_user(user) method
    #then this methode is called passing in the value returned rom User.get_id()
    #return User.query.get(user_id)
    return User.query.filter(User.email==user_id).first()

