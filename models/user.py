from app import db

class User(db.Model)
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)

    def __init__(self,email,password)
        self.email = email
        self.password = password

    def __repr__(self)
        return '<email {}'.format(self.email)
