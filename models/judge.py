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

#factory methods
def CreateActiveJudge(name,state,court,district,scope=1):
    return Judge(name=name,state=state,scope=scope,court=court,district=district)

def CreateRetiredJudge(name,state,scope=1):
    return Judge(name=name,state=state,scope=scope,retired=True)

def create_test_judges():
    judge = CreateActiveJudge(name="areg",state="CA",court="LA Superior", district="1st")
    db.session.add(judge)
    judge = CreateRetiredJudge(name="armen",state="CA")
    db.session.add(judge)
    db.session.commit()


