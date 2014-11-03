from flask import current_app
from plugins import db, bcrypt,login_manager,flaskuuid
from flask.ext.login import make_secure_token
from datetime import datetime
import uuid


class JudgeReview(db.Model):
    __tablename__ = "judgereviews"
    id = db.Column(db.Integer,primary_key=True)
    judge_id = db.Column(db.Integer,nullable=False)
    judge_name = db.Column(db.String(255),nullable=False)
    #body = db.Column(db.String(65535),nullable=False)
    excerpt = db.Column(db.String(255),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    reviewer_id = db.Column(db.Integer,nullable=False)
    reviewer_name = db.Column(db.String(255),nullable=False)
    active = db.Column(db.Boolean,nullable=False)
    removed = db.Column(db.Boolean,nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)

    #average of all the ratings below
    average_rating = db.Column(db.Integer,nullable=False)
    #ratings of range 1 to 5
    knowledge = db.Column(db.Integer,nullable=False)
    decorum = db.Column(db.Integer,nullable=False)
    tentatives = db.Column(db.Integer,nullable=False)
    curiosity = db.Column(db.Integer,nullable=False)



    # def __init__(self,body,rating,knowledge,decorum,tentatives,curiosity,
    #              judge_id, judge_name,reviewer_name,reviewer_id,title=None):
    #     self.judge_id = judge_id #judge.id
    #     self.judge_name = judge_name #judge.name
    #     excerpt_length = current_app.config['REVIEW_SUMMARY_LENGTH']
    #     self.excerpt = (body[:excerpt_length] + '...') if len(body) > excerpt_length else body
    #     self.body = body
    #     self.knowledge = knowledge
    #     self.decorum = decorum
    #     self.tentatives = tentatives
    #     self.curiosity = curiosity
    #     self.reviewer_name = reviewer_name #current_user.username
    #     self.reviewer_id = reviewer_id #current_user.id
    #     self.created_at = datetime.utcnow()
    #     self.active =  True
    #     self.removed = False
    #     ratings_total = knowledge + decorum + tentatives + curiosity
    #     self.average_rating = int(round(ratings_total / 4.0))

    def __init__(self,body,knowledge,decorum,tentatives,curiosity,
                 judge,reviewer,title=None):
        self.judge_id = judge.id
        self.judge_name = judge.name
        excerpt_length = current_app.config['REVIEW_SUMMARY_LENGTH']
        self.excerpt = (body[:excerpt_length] + '...') if len(body) > excerpt_length else body
        self.body = body
        self.knowledge = knowledge
        self.decorum = decorum
        self.tentatives = tentatives
        self.curiosity = curiosity
        self.reviewer_name = reviewer.username
        self.reviewer_id = reviewer.id
        self.created_at = datetime.utcnow()
        self.active =  True
        self.removed = False
        ratings_total = knowledge + decorum + tentatives + curiosity
        self.average_rating = int(round(ratings_total / 4.0))
        self.add_rating_averages(judge, reviewer)

    def average_rating_class(self):
        reviewrating = str(self.average_rating * 2)
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
        self.add_reviewer_rating_averages(reviewer)
        self.add_judge_rating_averages(judge)

    def add_reviewer_rating_averages(self, reviewer):
        #keep the total reviews count by the reviewer
        reviewer.total_reviews = reviewer.total_reviews + 1
        #keep a total of the average rating for each review by the reviewer
        reviewer.total_review_averages = reviewer.total_review_averages + self.average_rating
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_reviews_average =  reviewer.total_review_averages / reviewer.total_reviews
        #keep a total of the average rating for each review  by the reviewer
        reviewer.total_knowledges = reviewer.total_knowledges + self.knowledge
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_knowledges_average =  reviewer.total_knowledges / reviewer.total_reviews
        #keep a total of the average rating for each review by the reviewer
        reviewer.total_decorum = reviewer.total_decorum + self.decorum
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_decorum_average =  reviewer.total_decorum / reviewer.total_reviews
        #keep a total of the average rating for each review  by the reviewer
        reviewer.total_tentatives = reviewer.total_tentatives + self.tentatives
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_tentatives_average =  reviewer.total_tentatives / reviewer.total_reviews
        #keep a total of the average rating for each review for the judge
        reviewer.total_curiosity = reviewer.total_curiosity + self.curiosity
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_curiosity_average =  reviewer.total_curiosity / reviewer.total_reviews



    def add_judge_rating_averages(self, judge):
        #keep the total reviews count for the judge
        judge.total_reviews = judge.total_reviews + 1
        #keep a total of the average rating for each review for the judge
        judge.total_review_averages = judge.total_review_averages + self.average_rating
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_reviews_average =  judge.total_review_averages / judge.total_reviews
        #keep a total of the average rating for each review for the judge
        judge.total_knowledges = judge.total_knowledges + self.knowledge
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_knowledges_average =  judge.total_knowledges / judge.total_reviews
        #keep a total of the average rating for each review for the judge
        judge.total_decorum = judge.total_decorum + self.decorum
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_decorum_average =  judge.total_decorum / judge.total_reviews
        #keep a total of the average rating for each review for the judge
        judge.total_tentatives = judge.total_tentatives + self.tentatives
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_tentatives_average =  judge.total_tentatives / judge.total_reviews
        #keep a total of the average rating for each review for the judge
        judge.total_curiosity = judge.total_curiosity + self.curiosity
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_curiosity_average =  judge.total_curiosity / judge.total_reviews


    def edit_rating(self, body, judge, reviewer,knowledge,decorum,tentatives,curiosity):
        excerpt_length = current_app.config['REVIEW_SUMMARY_LENGTH']
        self.excerpt = (body[:excerpt_length] + '...') if len(body) > excerpt_length else body
        self.body = body
        #before updating the ratings and calculating the new average_rating
        self.reset_rating_averages(judge, reviewer)
        #next update the review ratings and rating average
        self.knowledge = knowledge
        self.decorum = decorum
        self.tentatives = tentatives
        self.curiosity = curiosity
        #calculate new total rating average average_rating
        ratings_total = knowledge + decorum + tentatives + curiosity
        self.average_rating = int(round(ratings_total / 4.0))
        #finally update the rating averages
        self.edit_rating_averages(judge, reviewer)


    def reset_rating_averages(self, judge, reviewer):
        self.reset_reviewer_rating_averages(reviewer)
        self.reset_judge_rating_averages(judge)

    def reset_reviewer_rating_averages(self,reviewer):
        #remove current rating average from rating average total
        reviewer.total_review_averages = reviewer.total_review_averages - self.average_rating
        #remove current knowledge rating from knowledge rating total
        reviewer.total_knowledges = reviewer.total_knowledges - self.knowledge
        reviewer.total_decorum = reviewer.total_decorum - self.decorum
        reviewer.total_tentatives = reviewer.total_tentatives - self.tentatives
        reviewer.total_curiosity = reviewer.total_curiosity - self.curiosity

    def reset_judge_rating_averages(self, judge):
        #remove current rating average from rating average total
        judge.total_review_averages = judge.total_review_averages - self.average_rating
        #remove current knowledge rating from knowledge rating total
        judge.total_knowledges = judge.total_knowledges - self.knowledge
        judge.total_decorum = judge.total_decorum - self.decorum
        judge.total_tentatives = judge.total_tentatives - self.tentatives
        judge.total_curiosity = judge.total_curiosity - self.curiosity

    def edit_rating_averages(self, judge, reviewer):
        self.add_reviewer_rating_averages(reviewer)
        self.add_judge_rating_averages(judge)

    def edit_reviewer_rating_averages(self,reviewer):
        #keep a total of the average rating for each review by the reviewer
        reviewer.total_review_averages = reviewer.total_review_averages + self.average_rating
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_reviews_average =  reviewer.total_review_averages / reviewer.total_reviews
        #keep a total of the average rating for each review  by the reviewer
        reviewer.total_knowledges = reviewer.total_knowledges + self.knowledge
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_knowledges_average =  reviewer.total_knowledges / reviewer.total_reviews
        #keep a total of the average rating for each review by the reviewer
        reviewer.total_decorum = reviewer.total_decorum + self.decorum
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_decorum_average =  reviewer.total_decorum / reviewer.total_reviews
        #keep a total of the average rating for each review  by the reviewer
        reviewer.total_tentatives = reviewer.total_tentatives + self.tentatives
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_tentatives_average =  reviewer.total_tentatives / reviewer.total_reviews
        #keep a total of the average rating for each review for the judge
        reviewer.total_curiosity = reviewer.total_curiosity + self.curiosity
        #calculate the average of all the average ratings of the reviews by the reviewer
        reviewer.total_curiosity_average =  reviewer.total_curiosity / reviewer.total_reviews



    def edit_judge_rating_averages(self, judge):
        #keep a total of the average rating for each review for the judge
        judge.total_review_averages = judge.total_review_averages + self.average_rating
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_reviews_average =  judge.total_review_averages / judge.total_reviews
        #keep a total of the average rating for each review for the judge
        judge.total_knowledges = judge.total_knowledges + self.knowledge
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_knowledges_average =  judge.total_knowledges / judge.total_reviews
        #keep a total of the average rating for each review for the judge
        judge.total_decorum = judge.total_decorum + self.decorum
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_decorum_average =  judge.total_decorum / judge.total_reviews
        #keep a total of the average rating for each review for the judge
        judge.total_tentatives = judge.total_tentatives + self.tentatives
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_tentatives_average =  judge.total_tentatives / judge.total_reviews
        #keep a total of the average rating for each review for the judge
        judge.total_curiosity = judge.total_curiosity + self.curiosity
        #calculate the average of all the average ratings of the reviews for the judge
        judge.total_curiosity_average =  judge.total_curiosity / judge.total_reviews

