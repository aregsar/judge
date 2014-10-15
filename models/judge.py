from plugins import db, bcrypt,login_manager,flaskuuid
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
    total_reviews = db.Column(db.Integer,nullable=False)
    total_review_averages = db.Column(db.Integer,nullable=False)
    total_reviews_average = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)

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

    def total_reviews_average_class(self):
        judgerating = str(self.total_reviews_average * 2)
        return 'clip-' + judgerating + ' pos-' + judgerating

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


