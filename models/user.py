from app import db

@login_manager.user_loader
def user_loader(user_id):
    #user_id is the value returned from User.get_id() method
    #it is first called by flask-login in the login_user(user) method
    #then this methode is called passing in the value returned rom User.get_id()
    return User.query.get(user_id)

class User(db.Model)
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),nullable=False)
    barnumber = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    user_role = db.Column(db.String,nullable=False)#options: "member" or "mod" or "admin" or "sa"
    signin_token = db.Column(db.String,nullable=False)
    #signedin_at = db.Column(db.DateTime,nullable=False)
    activated = db.Column(db.Boolean,nullable=False)
    #activated_at = db.Column(db.DateTime,nullable=False)
    banned = db.Column(db.Boolean,nullable=False)

    authenticated = False


    def __init__(self,email,password,barnumber,username):
        self.email = email
        self.password = password
        self.barnumber = barnumber
        self.username = username
        self.user_role = "member"
        self.signin_token = ""
        self.activated = True;#TODO:default to false
        self.banned = False;


    def is_not_banned():
        #return self.banned
        return True

    def password_is_authenticated(pasword):
        hashedpassword = "areg"
        #hashedpassword = compute_hash(password)
        return self.password == hashedpassword

    def refresh_signin_token_and_date():
        self.signin_token = "areg"
        #self.signedin_at = DateTime.utcnow

    #Flask-Login interface
    def get_id(self):

        #return self.email
        unicode(self.id)

    def is_active(self):
        return self.activated

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    #end Flask-Login interface

    def __repr__(self)
        return '<email {}'.format(self.email)
