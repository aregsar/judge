from plugins import db, bcrypt,login_manager,flaskuuid
from flask.ext.login import make_secure_token
from datetime import datetime
import uuid

class Candidate(db.Model):
     __tablename__ = "candidate"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False,  index=True)
    state = db.Column(db.String(20),nullable=False)
