from flask import Blueprint,render_template,g, current_app
from flask.ext.login import current_user
from forms.account.signin_form import SigninForm
from forms.judge.judge_search_form import JudgeSearchForm
from forms.account import signup_form

#bluprint is registered in blueprints.py
res = Blueprint('home',__name__)


#uncomment for blueprint specific error handler
#@mod.app_errorhandler(404)
#def not_found(e):
    #return render_template("home/404.html")


@res.route('/')
def index():
    if current_user.is_authenticated():
        form = JudgeSearchForm()
        return render_template("home/dashboard.html",form=form)
    else:
        form = signup_form.SignupForm()
        return render_template("account/signup.html",form=form)



