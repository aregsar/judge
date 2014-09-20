from flask import Blueprint,render_template,g,request
from forms.signin_form import SigninForm
from flask.ext.login import current_user
from forms.judge_search_form import JudgeSearchForm
from flask.ext.login import LoginManager,login_required,login_user,logout_user
from plugins import db

from models.judge import Judge, CreateRetiredJudge

mod = Blueprint('judge',__name__)



@mod.route('/judge')
@login_required
def index():

    #print current_user
    if current_user.is_authenticated():
        name = request.args.get('name')

        # judge = CreateRetiredJudge(name=name,state="CA")
        # db.session.add(judge)
        # db.session.commit()

        form = JudgeSearchForm(name=name)
        judges= Judge.query.filter_by(name=name).all()
        message = None
        if len(judges) == 0:
            message = "Didn't find your judge? Submit them for review by clicking here."

        return render_template("judge/index.html",form=form,judges=judges,name=name,message=message)

