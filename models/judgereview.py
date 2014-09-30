from plugins import db, bcrypt,login_manager,flaskuuid
from flask.ext.login import make_secure_token
from datetime import datetime
import uuid


class JudgeReview(db.Model):
    __tablename__ = "judgereviews"
    id = db.Column(db.Integer,primary_key=True)
    judge_id = db.Column(db.Integer,nullable=False)
    judge_name = db.Column(db.String(255),nullable=False)
    title = db.Column(db.String(255),nullable=False)
    #body = db.Column(db.String(65535),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    #rating of range 1 to 5
    rating = db.Column(db.Integer,nullable=False)
    knowledge = db.Column(db.Integer,nullable=False)
    decorum = db.Column(db.Integer,nullable=False)
    tentatives = db.Column(db.Integer,nullable=False)
    curiosity = db.Column(db.Integer,nullable=False)
    reviewer_id = db.Column(db.Integer,nullable=False)
    reviewer_name = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)
    active = db.Column(db.Boolean,nullable=False)
    removed = db.Column(db.Boolean,nullable=False)

    #def __init__(self,title,body,rating,judge,current_user):
    def __init__(self,title,body,rating,knowledge,decorum,tentatives,curiosity,
                 judge_id, judge_name,reviewer_name,reviewer_id):
        self.title = title
        self.judge_id = judge_id #judge.id
        self.judge_name = judge_name #judge.name
        self.body = body
        self.rating = rating
        self.knowledge = knowledge
        self.decorum = decorum
        self.tentatives = tentatives
        self.curiosity = curiosity
        self.reviewer_name = reviewer_name #current_user.username
        self.reviewer_id = reviewer_id #current_user.id
        self.created_at = datetime.utcnow()
        self.active =  False
        self.removed = False
