from app import db

class User(db.Model)
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),nullable=False)
    barnumber = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    signin_token = db.Column(db.String,nullable=False)
    user_role = db.Column(db.String,nullable=False)#options: "user" or "mod" or "admin" or "sa"
    activated = db.Column(db.Boolean,nullable=False)
    banned = db.Column(db.Boolean,nullable=False)
    activated_at = db.Column(db.DateTime,nullable=False)
    signedin_at = db.Column(db.DateTime,nullable=False)

    def __init__(self,email,password)
        self.email = email
        self.password = password


    def is_active(self):
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self)
        return '<email {}'.format(self.email)
