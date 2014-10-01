from plugins import db, bcrypt,login_manager,flaskuuid
from flask.ext.login import make_secure_token
from flask.ext.login import current_user
from datetime import datetime
import uuid


#User.__table__
#User.__mapper__

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(255),nullable=False)
    lastname = db.Column(db.String(255),nullable=False)
    state = db.Column(db.String(2),nullable=False)
    username = db.Column(db.String(255),nullable=False, unique=True, index=True)
    barnumber = db.Column(db.String(255),nullable=False, unique=True, index=True)
    email = db.Column(db.String(255),nullable=False, unique=True, index=True)
    password = db.Column(db.String(2048),nullable=False)
    password_reset_token = db.Column(db.String(2048),nullable=True, unique=True, index=True)
    user_role = db.Column(db.String(50),nullable=False) #options: "member" or "mod" or "admin" or "sa"
    approved = db.Column(db.Boolean,nullable=False)
    approved_at = db.Column(db.DateTime,nullable=True)
    activation_token = db.Column(db.String(2048),nullable=True, unique=True, index=True)
    activated = db.Column(db.Boolean,nullable=False)
    activated_at = db.Column(db.DateTime,nullable=True)
    signin_token = db.Column(db.String(2048),nullable=True, unique=True, index=True)
    signedin_at = db.Column(db.DateTime,nullable=True)
    banned = db.Column(db.Boolean,nullable=False)
    lastvisit_at = db.Column(db.DateTime,nullable=True)
    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)

    #SecureRandom.urlsafe_base64

    #used to set the state of this object before passing it to flask logins login_user method
    authenticated = False

    def __init__(self,email,password,barnumber,username,firstname,lastname,state):
        self.firstname = firstname
        self.lastname = lastname
        self.state = state
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
        self.lastvisit_at = None
        self.approved = False
        self.approved_at = None


    def set_password(self,password):
        self.password = bcrypt.generate_password_hash(password)

    def approve(self):
        dt = datetime.utcnow()
        self.approved = True
        self.approved_at = dt
        self.updated_at = dt

    def activate(self):
        if self.approved:
            dt = datetime.utcnow()
            self.activated = True
            self.activated_at = dt
            self.updated_at = dt

    def refresh_signin_token_and_date(self):
        dt = datetime.utcnow()
        guid = uuid.uuid4().hex
        print guid
        self.signin_token = make_secure_token(guid)
        self.signedin_at = dt
        self.updated_at = dt

    def is_banned(self):
        return self.banned


    def ban(self):
        if self.user_role != "admin":
            if current_user.user_role == "admin":
                self.banned = True
                self.updated_at = datetime.utcnow()
    def unban(self):
        if current_user.user_role == "admin":
            self.banned = False
            self.updated_at = datetime.utcnow()

    #Flask-Login interface
    def get_id(self):
        return unicode(self.signin_token)
        #return unicode(self.email)
        #return unicode(self.id)

    def is_active(self):
        return self.activated and not self.banned

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
    #flask login api for alternative token authentication
    #not used since we are just returning the token via get_id
    #def get_auth_token(self)
    #   return unicode(self.signin_token)

    #end Flask-Login interface

    def __repr__(self):
        return '<email {}>'.format(self.email)

    def show_email(self,viewer):
        if viewer.user_role == "admin":
            return self.email
        return ''


#factory method
def create_test_users():
    user = User(
            email = "aregsar@gmail.com",
            password = "panama",
            barnumber = "1234",
            firstname = "aregsar",
            lastname = "sarkissian",
            state = "CA",
            username = "aregsar")
    user.approve()
    user.activate()
    user.user_role = "admin"
    db.session.add(user)
    db.session.commit()
    user = User(
            email = "areg@cox.com",
            password = "panama",
            barnumber = "12345",
            firstname = "areg",
            lastname = "sarkissian",
            state = "CA",
            username = "areg")
    user.approve()
    user.activate()
    db.session.add(user)
    db.session.commit()


#flask login api for user if based authentication. works in conjunction with get_id
#hacked it so it uses tokens instead of user id
#define after defining User
@login_manager.user_loader
def user_loader(user_id):
    #user_id is the value returned from User.get_id() method
    #it is first called by flask-login in the login_user(user) method
    #then this methode is called passing in the value returned rom User.get_id()
    #return User.query.get(user_id)
    user = User.query.filter(User.signin_token==user_id).first()
    #user = User.query.filter(User.email==user_id).first()
    if user:
        user.authenticated = True
        #print user.lastvisit_at
        #user.lastvisit_at = datetime.utcnow()
        #db.session.commit()
    return user


#flask login api for alternative token authentication. works in conjunction with get_auth_token
#not used since we are using user_loader passing in a token via user_id
#@login_manager.token_loader
#def token_loader(user_token):
    # user = User.query.filter(User.signin_token==user_token).first()
    # if user:
    #     user.authenticated = True
    # return user

