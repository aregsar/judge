from flask import Blueprint,render_template,g,request
from forms.signin_form import SigninForm
from flask.ext.login import current_user
from forms.judge_search_form import JudgeSearchForm
from forms.judge_submit_form import JudgeSubmitForm
from flask.ext.login import LoginManager,login_required,login_user,logout_user
from plugins import db
from models.judge import Judge, CreateRetiredJudge
from models.candidate import Candidate
#this bluprint is registered in blueprints.py
mod = Blueprint('judge',__name__)



@mod.route('/judge')
@login_required
def index():
    #if current_user.is_authenticated():
    name = request.args.get('name')
    form = JudgeSearchForm(name=name)
    judges= Judge.query.filter_by(name=name).all()
    message = None
    if len(judges) == 0:
        message = "Didn't find your judge? Submit them for review by clicking here."
    return render_template("judge/index.html",form=form,judges=judges,name=name,message=message)

@mod.route('/judge/submit/<name>',methods=['GET','POST'])
@login_required
def submit(name):
    form = JudgeSubmitForm(name=name)
    if form.validate_on_submit():
        judge = Candidate(name=name)
        db.session.add(judge)
        db.session.commit()
        return render_template("judge/submitted.html")
    return render_template("judge/submit.html",form=form,name=name)

