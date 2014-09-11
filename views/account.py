from flask import Blueprint,redirect, render_template, url_for, g, current_app
import uuid
from plugins import db, flaskuuid

#NameError: global name 'SigninForm' is not defined
#from forms import signin_form, signup_form, forgotpassword_form
from forms.signin_form import SigninForm
from forms.signup_form import SignupForm
from forms.forgotpassword_form import ForgotPasswordForm

mod = Blueprint('account',__name__)


#using flask-uuid
#@app.route('/<uuid(strict=False):id>'>
#@app.route('/<uuid:id>')
#def mypage(id):
#    return id  # 'id' is a uuid.UUID instance
#import uuid
#url_for('mypage', id=uuid.uuid4())



@mod.route('/account/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("account.signedup"))
    return render_template("account/signup.html",form=form)


@mod.route('/account/password/reset',methods=['GET','POST'])
def forgot_password():
    form = ForgotPasswordForm()
    #if True:
    #    return redirect(url_for("account.signedup"))
    return render_template("account/forgot_password.html",form=form)


@mod.route('/account/signin',methods=['GET','POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if (user
            and user.is_not_banned()
            and user.password_is_authenticated(form.password.data) ):
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            #store the authentcation state for login_user
            user.authenticated=True
            login_user(user, remember=True)
            return redirect(url_for("home.index"))
    #flash "invalid email or password"
    return render_template("account/signin.html",form=form)


#@login_required
def logout():
    logout_user()
    return render_template("home/index.html")


@mod.route('/account/signedup')
def signedup():
    return render_template("account/signedup.html")

@mod.route('/account/confirm',methods=['GET','POST'])
def confirm():
    return render_template("account/account_confirmed.html")

    #if False:
    #    return redirect(url_for("home.dashboard"))
    #return render_template("account/account_confirmation_error.html")

