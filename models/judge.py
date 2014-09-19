from plugins import db, bcrypt,login_manager,flaskuuid
from flask.ext.login import make_secure_token
from datetime import datetime
import uuid

class Judge(db.Model):
    __tablename__ = "judges"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False,  index=True)

    #for ative judges scope options are federal or state
    #for retired judges scope options are mediator, arbitrator, both
    scope = db.Column(db.String(255),nullable=False)
    retired = db.Column(db.Boolean,nullable=False)
    state = db.Column(db.String(20),nullable=False)
    #court is null for retured judges
    court = db.Column(db.String(255),nullable=True,  index=True)
    #district options are appelate, suprerior (or null for retired judges)
    district = db.Column(db.String(255),nullable=True)

    created_at = db.Column(db.DateTime,nullable=False, index=True)
    updated_at = db.Column(db.DateTime,nullable=True)

    def __init__(self,name,scope,state=None,retired=False,court=None,district=None):
        self.name = name
        self.scope = scope
        self.state = state
        self.retired = retired
        self.court = court
        self.district = district
        self.created_at = datetime.utcnow()

#factory methods
def CreateActiveJudge(name,state,court,district,scope="State"):
    return Judge(name="areg",scope=scope,state=state,court=court,district=district)

def CreateRetiredJudge(name,scope="Arbitrator"):
    return Judge(name=name,scope=scope,retired=True)
