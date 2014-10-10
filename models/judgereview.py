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
    excerpt = db.Column(db.String(255),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    #rating of range 1 to 5
    rating = db.Column(db.Integer,nullable=False)
    knowledge = db.Column(db.Integer,nullable=False)
    decorum = db.Column(db.Integer,nullable=False)
    tentatives = db.Column(db.Integer,nullable=False)
    curiosity = db.Column(db.Integer,nullable=False)
    reviewer_id = db.Column(db.Integer,nullable=False)
    reviewer_name = db.Column(db.String(255),nullable=False)
    active = db.Column(db.Boolean,nullable=False)
    removed = db.Column(db.Boolean,nullable=False)
    average_rating = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)


    #def __init__(self,title,body,rating,judge,current_user):
    def __init__(self,body,rating,knowledge,decorum,tentatives,curiosity,
                 judge_id, judge_name,reviewer_name,reviewer_id,title=None):
        self.title = ''
        self.judge_id = judge_id #judge.id
        self.judge_name = judge_name #judge.name
        self.excerpt = (body[:10] + '...') if len(body) > 10 else body
        self.body = body
        self.rating = rating
        self.knowledge = knowledge
        self.decorum = decorum
        self.tentatives = tentatives
        self.curiosity = curiosity
        self.reviewer_name = reviewer_name #current_user.username
        self.reviewer_id = reviewer_id #current_user.id
        self.created_at = datetime.utcnow()
        self.active =  True
        self.removed = False

        ratings_total = rating + knowledge + decorum + tentatives + curiosity
        self.average_rating = int(round(ratings_total / 5.0))

    def average_rating_class(self):
        reviewrating = str(self.average_rating * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

    def rating_class(self):
        reviewrating = str(self.rating * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

    def knowledge_class(self):
        reviewrating = str(self.knowledge * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating
    def decorum_class(self):
        reviewrating = str(self.decorum * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

    def tentatives_class(self):
        reviewrating = str(self.tentatives * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

    def curiosity_class(self):
        reviewrating = str(self.curiosity * 2)
        return 'clip-' + reviewrating + ' pos-' + reviewrating

    def add_rating_averages(self, judge, reviewer):
        reviewer.total_reviews = reviewer.total_reviews + 1
        reviewer.total_review_averages = reviewer.total_review_averages + self.average_rating
        reviewer.total_reviews_average =  reviewer.total_review_averages / reviewer.total_reviews
        judge.total_reviews = judge.total_reviews + 1
        judge.total_review_averages = judge.total_review_averages + self.average_rating
        judge.total_reviews_average =  judge.total_review_averages / judge.total_reviews



    def edit_rating(self, body, judge, reviewer,rating,knowledge,decorum,tentatives,curiosity):
        self.excerpt = (body[:10] + '...') if len(body) > 10 else body
        self.body = body
        #remove current rating average from total
        reviewer.total_review_averages = reviewer.total_review_averages - self.average_rating
        judge.total_review_averages = judge.total_review_averages - self.average_rating
        #calculate new total rating average
        ratings_total = rating + knowledge + decorum + tentatives + curiosity
        self.average_rating = int(round(ratings_total / 5.0))
        #update the total averages
        reviewer.total_review_averages = reviewer.total_review_averages + self.average_rating
        reviewer.total_reviews_average =  reviewer.total_review_averages / reviewer.total_reviews
        judge.total_review_averages = judge.total_review_averages + self.average_rating
        judge.total_reviews_average =  judge.total_review_averages / judge.total_reviews
