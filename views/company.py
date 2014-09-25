from flask import Blueprint,render_template,g

#NameError: global name 'SigninForm' is not defined
#from forms import signin_form
from forms.signin_form import SigninForm
from forms.judge_search_form import JudgeSearchForm
from flask.ext.login import current_user


#this bluprint is registered in blueprints.py
mod = Blueprint('company',__name__)


#uncomment for blueprint specific error handler
#@mod.app_errorhandler(404)
#def not_found(e):
    #return render_template("home/404.html")


@mod.route('/about')
def about():
    return render_template('company/about.html')

@mod.route('/contact')
def contact():
    return render_template('company/contact.html')

@mod.route('/terms')
def terms():
    return render_template('company/terms.html')

@mod.route('/privacy')
def privacy():
    return render_template('company/privacy.html')

@mod.route('/security')
def security():
    return render_template('company/security.html')



