from flask import Blueprint,render_template,g
from forms.signin_form import SigninForm
from flask.ext.login import current_user
from forms.judge_search_form import JudgeSearchForm
from flask.ext.login import LoginManager,login_required,login_user,logout_user

mod = Blueprint('judge',__name__)


#@login_required
@mod.route('/judge/<judgename>')
def index(judgename):
    print current_user
    print "judggeds"
    if current_user.is_authenticated():
        form = JudgeSearchForm(name=judgename)
        judges=None #Judge.query.filter_by(judgename=name).all()
        return render_template("home/dashboard.html",form=form,judges=judges)

