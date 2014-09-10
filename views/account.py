from flask import Blueprint,redirect, render_template, url_for,g
import uuid
from services import db,flaskuuid

mod = Blueprint('account',__name__)



#using flask-uuid
#@app.route('/<uuid(strict=False):id>'>
#@app.route('/<uuid:id>')
#def mypage(id):
#    return id  # 'id' is a uuid.UUID instance
#import uuid
#url_for('mypage', id=uuid.uuid4())

#@mod.route('/account/signin')
@mod.route('/account/signin')
def signin():
    if True:
        return redirect(url_for("home.dashboard"))
    return redirect(url_for("home.dashboard"))
    #flash message signup error
    #return render_template("account/signup_error.html")

@mod.route('/account/signup')
def signup():
    if True:
        return redirect(url_for("account.signedup"))
    return render_template("account/signup.html")

@mod.route('/account/signedup')
def signedup():
    return render_template("account/signedup.html")

@mod.route('/account/confirm',methods=['GET','POST'])
def confirm():
    return render_template("account/account_confirmed.html")

    #if False:
    #    return redirect(url_for("home.dashboard"))
    #return render_template("account/account_confirmation_error.html")

