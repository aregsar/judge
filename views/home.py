from flask import Blueprint,render_template,g

#NameError: global name 'SigninForm' is not defined
#from forms import signin_form
from forms.signin_form import SigninForm
from forms.judge_search_form import JudgeSearchForm
from flask.ext.login import current_user
mod = Blueprint('home',__name__)


#uncomment for blueprint specific error handler
#@mod.app_errorhandler(404)
#def not_found(e):
    #return render_template("home/404.html")


@mod.route('/')
def index():
    print current_user
    #1/0
    #return 'home.index'
    #abort(404)
    #print g.current_user

    if current_user.is_authenticated():
        form = JudgeSearchForm()
        return render_template("home/dashboard.html",form=form)
    else:
        #must pass an empty form for antiXSS
        form = SigninForm()
        return render_template("home/index.html",form=form)


@mod.route('/dashboard')
def dashboard():
    return render_template("home/dashboard.html")

