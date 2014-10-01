from plugins import db, bcrypt,login_manager,flaskuuid
from flask.ext.login import make_secure_token
from datetime import datetime
import uuid

class UserJudge(db.Model):
    __tablename__ = "userjudges"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,nullable=False)
    judge_id = db.Column(db.Integer,nullable=False)
    judge_name = db.Column(db.String(255),nullable=False,  index=True)
    removed = db.Column(db.Boolean,nullable=False)

    def __init__(self,user_id,judge_id,judge_name):
        self.user_id = user_id
        self.judge_id = judge_id
        self.judge_name = judge_name
        self.removed = False

