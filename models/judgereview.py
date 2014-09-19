from plugins import db, bcrypt,login_manager,flaskuuid
from flask.ext.login import make_secure_token
from datetime import datetime
import uuid

class JudgeReview(db.Model):
    __tablename__ = "judgereviews"
    id = db.Column(db.Integer,primary_key=True)
    judge_id = db.Column(db.Integer,nullable=False)
    title = db.Column(db.String(255),nullable=False)
    #body = db.Column(db.String(65535),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    #rating of range 1 to 5
    rating = db.Column(db.Integer,nullable=False)
    #username of reviewer
    created_by = db.Column(db.String(255),nullable=False)
    #user id of reviewer
    created_by_id = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)

    #def __init__(self,judge_id,title,body,rating,user):
    def __init__(self,judge_id,title,body,rating,username,user_id):
        self.title = title
        self.judge_id = judge_id
        self.body = body
        self.rating = rating
        # self.created_by = user.username
        # self.created_by_id = user.id
        self.created_by = username
        self.created_by_id = user_id
        self.created_at = datetime.utcnow()
