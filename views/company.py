from flask import Blueprint,render_template,g


#this bluprint is registered in blueprints.py
mod = Blueprint('company',__name__)


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



