from plugins import db, bcrypt,login_manager,flaskuuid, current_app
from flask.ext.login import make_secure_token
from datetime import datetime
import uuid

class Judge(db.Model):
    __tablename__ = "judges"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False,  index=True)

    #for ative judges scope options are 1-federal or 2-state
    #for retired judges scope options are 1-mediator, 2-arbitrator, 3-both
    scope = db.Column(db.Integer,nullable=False)
    retired = db.Column(db.Boolean,nullable=False)
    state = db.Column(db.String(20),nullable=False)
    #court is null for retured judges
    court = db.Column(db.String(255),nullable=True,  index=True)
    #district options are appelate, suprerior (or null for retired judges)
    district = db.Column(db.String(255),nullable=True)
    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)
    #this the total number of reviews
    total_reviews = db.Column(db.Integer,nullable=False)
    #this is the total of the average rating for each review for this judge
    total_review_averages = db.Column(db.Integer,nullable=False)
    #this is the average of the average rating for each review for this judge i.e.(total_review_averages\total_reviews)
    total_reviews_average = db.Column(db.Integer,nullable=False)

    #this is the total of the knowledge rating for each review for this judge
    total_knowledges = db.Column(db.Integer,nullable=False)
    #this is the average of the knowledge rating for each review for this judge i.e (total_knowledges\total_reviews)
    total_knowledges_average = db.Column(db.Integer,nullable=False)
    total_decorum = db.Column(db.Integer,nullable=False)
    total_decorum_average = db.Column(db.Integer,nullable=False)
    total_tentatives = db.Column(db.Integer,nullable=False)
    total_tentatives_average  = db.Column(db.Integer,nullable=False)
    total_curiosity = db.Column(db.Integer,nullable=False)
    total_curiosity_average  = db.Column(db.Integer,nullable=False)


    def __init__(self,name,state,scope,retired=False,court=None,district=None):
        self.name = name
        self.scope = scope
        self.state = state
        self.retired = retired
        self.court = court
        self.district = district
        self.created_at = datetime.utcnow()
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

    # def total_reviews_average_clip(self):
    #     return 'clip-' + str(self.total_reviews_average)

    # def total_reviews_average_pos(self):
    #     return 'pos-' + str(self.total_reviews_average)

    def __repr__(self):
        return '<name={name}  \
            ,court={court}  \
            ,state={state}  \
            >'.format(name=self.name,
            court=self.court,
            state=self.state)

#factory methods
def CreateActiveJudge(name,state,court,district,scope=1):
    return Judge(name=name,state=state,scope=scope,court=court,district=district)

def CreateRetiredJudge(name,state,scope=1):
    return Judge(name=name,state=state,scope=scope,retired=True)

def create_test_judges():
    judge = CreateActiveJudge(name="bob",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateActiveJudge(name="bill",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateActiveJudge(name="john",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateActiveJudge(name="paul",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateActiveJudge(name="george",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateActiveJudge(name="ringo",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateActiveJudge(name="kim",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateActiveJudge(name="judy",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateRetiredJudge(name="ben",state="CA")
    db.session.add(judge)
    judge = CreateRetiredJudge(name="jane",state="CA")
    db.session.add(judge)
    judge = CreateRetiredJudge(name="jill",state="CA")
    db.session.add(judge)
    judge = CreateRetiredJudge(name="adam",state="CA")
    db.session.add(judge)
    judge = CreateRetiredJudge(name="joe",state="CA")
    db.session.add(judge)
    judge = CreateRetiredJudge(name="mike",state="CA")
    db.session.add(judge)
    db.session.commit()


