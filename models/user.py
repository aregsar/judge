from flask import current_app
from plugins import db, bcrypt,login_manager,flaskuuid
from flask.ext.login import make_secure_token
from flask.ext.login import current_user
from datetime import datetime
import uuid
from models.state import STATE_CHOICES_DICT


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

    #this the total number of reviews
    total_reviews = db.Column(db.Integer,nullable=False)
    #this is the total of the average rating for each review by this user
    total_review_averages = db.Column(db.Integer,nullable=False)
    #this is the average of the average rating for each review by this user i.e.(total_review_averages\total_reviews)
    total_reviews_average = db.Column(db.Integer,nullable=False)


    #this is the total of the knowledge rating for each review by this user
    total_knowledges = db.Column(db.Integer,nullable=False)
    #this is the average of the knowledge rating for each review by this user i.e (total_knowledges\total_reviews)
    total_knowledges_average = db.Column(db.Integer,nullable=False)
    total_decorum = db.Column(db.Integer,nullable=False)
    total_decorum_average = db.Column(db.Integer,nullable=False)
    total_tentatives = db.Column(db.Integer,nullable=False)
    total_tentatives_average  = db.Column(db.Integer,nullable=False)
    total_curiosity = db.Column(db.Integer,nullable=False)
    total_curiosity_average  = db.Column(db.Integer,nullable=False)

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
        self.approved = True
        self.approved_at = self.created_at
        self.total_reviews = 0
        self.total_review_averages = 0
        #total_reviews_average = total_review_averages/total_reviews
        self.total_reviews_average = 0
        self.total_knowledges = 0
        self.total_knowledges_average = 0
        self.total_decorum = 0
        self.total_decorum_average = 0
        self.total_tentatives = 0
        self.total_tentatives_average  = 0
        self.total_curiosity = 0
        self.total_curiosity_average  = 0

    def make_active(self):
        self.approve()
        self.activate()
        self.refresh_signin_token_and_date()

    #return a string containing two css classes example: "clip-2 pos-2"
    def total_reviews_average_class(self):
        #there are 10 rows of 5 gavel rating bitmaps.(first row 0 gavels is not used)
        #0 gvls, 1 gvl,1.5 gvls, 2 gvls,2.5 gvls, 3 gvls, 3.5 gvls, 4 gvls, 4.5 gvls, 5gvls
        #ratings selections are 1 to 5 so since we dont use the 0 gavels first bitmap row
        #we multipy the rating by two to get the rating bitmap row number starting with row 2:
        #1 * 2 = row 2, 1.5 * 2 = row 3, 2 * 2 = row 4, ..., 4.5 * 2 = row 9, 5 * 2 = row 10
        judgerating = str(self.total_reviews_average * 2)
        #clip-n class will clip the nth row and
        #pos-n class will shift the n-th row to position 0 in the browser viewport
        return 'clip-' + judgerating + ' pos-' + judgerating

    def knowledge_class(self):
        reviewrating = str(self.total_knowledges_average * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

    def decorum_class(self):
        reviewrating = str(self.total_decorum_average * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

    def tentatives_class(self):
        reviewrating = str(self.total_tentatives_average * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

    def curiosity_class(self):
        reviewrating = str(self.total_curiosity_average * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

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
        #print guid
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
        return self.approved and not self.banned

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



    def update_password(password):
        self.set_password(password)
        self.refresh_signin_token_and_date()
        try:
            db.session.commit()
            return True
        except:
            return False


    @staticmethod
    def reset_password(password_reset_form):
        state = password_reset_form.state.data.strip().upper()
        if state not in STATE_CHOICES_DICT:
            return None, "invalid state abbreviation"
        user = User.query.filter_by(email=password_reset_form.email.data.strip()).first()
        if user:
            if user.valid_password_reset_credentials(password_reset_form):
                user.set_password(password_reset_form.password.data.strip())
                user.refresh_signin_token_and_date()
                try:
                    db.session.commit()
                    return user, ""
                except:
                    return None, "there was an error updating your password. please try again"
            return None, "credentials provided do not match those on file"
        return None, "could not find user account with email"

    def valid_password_reset_credentials(self,password_reset_form):
        if (self.barnumber == password_reset_form.barnumber.data.strip() and
                    self.username.lower() == password_reset_form.username.data.strip().lower() and
                    self.firstname.lower() == password_reset_form.firstname.data.strip().lower() and
                    self.lastname.lower() == password_reset_form.lastname.data.strip().lower() and
                    self.state.lower() == password_reset_form.state.data.strip().lower()):
            return True
        return False


    @staticmethod
    def signin(signinform):
        user = User.query.filter_by(email=signinform.email.data.strip()).first()
        if user:
            if bcrypt.check_password_hash(user.password, signinform.password.data.strip()):
                user.refresh_signin_token_and_date()
                db.session.commit()
                #store the authentcation state for login_user
                #to access via user.is_authenticated()
                user.authenticated=True


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
