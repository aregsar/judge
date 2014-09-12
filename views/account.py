from flask import Blueprint,redirect, render_template, url_for, g, current_app
import uuid
from plugins import db, flaskuuid
#NameError: global name 'SigninForm' is not defined
#from forms import signin_form, signup_form, forgotpassword_form
from forms.signin_form import SigninForm
from forms.signup_form import SignupForm
from forms.forgotpassword_form import ForgotPasswordForm
from itsdangerous import URLSafeTimedSerializer
from flask.ext.login import LoginManager

secret = current_app.config["SECRET_KEY"]
ts = URLSafeTimedSerializer(secret)

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
         user = User(
            email = form.email.data,
            password = form.password.data,
            barnumber=form.barnumber.data,
            username=form.username.data
        )
        db.session.add(user)
        db.session.commit()
        token = ts.dumps(self.email, salt=secret)
        confirm_url = url_for('account.confirm',token=token,_external=True)
        #html = render_template('account/confirm.html',confirm_url=confirm_url)
        #send_email(user.email, subject, html)
        return render_template("account/confirm.html",confirm_url=confirm_url)
    return render_template("account/signup.html",form=form)

@app.route('/account/confirm/<token>')
def confirm_account(token):
    try:
        email = ts.loads(token, salt=secret, max_age=86400)
    except:
        abort(404)
        #redirect(url_for(account.invalid_token))

    user = User.query.filter_by(email=email).first_or_404()
    user.verified = True
    db.session.add(user)
    db.session.commit()
    form = SigninForm()
    #return redirect(url_for('account.signin'))
    flash("Account verified. Please sign in")
    return render_template("account/signin.html",form=form)



@mod.route('/account/password/activate',methods=['GET','POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first_or_404()
        if user.is_not_banned():
            token = ts.dumps(self.email, salt=secret)
            if user.activated:
                password_url = url_for('account.reset_password',token=token,_external=True)
                #html = render_template('account/reset_password.html',password_url=password_url)
                return render_template("account/reset_password.html",password_url=password_url)
            else
                confirm_url = url_for('account.confirm',token=token,_external=True)
                #html = render_template('account/confirm.html',confirm_url=confirm_url)
                return render_template("account/confirm.html",confirm_url=confirm_url)
            #send_email(user.email, subject, html)
    return render_template("account/forgot_password.html",form=form)



@app.route('/account/password/reset/<token>')
def reset_password(token):
    try:
        email = ts.loads(token, salt=secret, max_age=86400)
    except:
        abort(404)
        #redirect(url_for(account.invalid_token))

    form = SetPasswordForm()
    #form.token.data = token
    return render_template("account/set_password.html",form=form,token=token)

@mod.route('/account/password/set/<token>',methods=['GET','POST'])
def set_password():
    try:
        email = ts.loads(token, salt=secret, max_age=86400)
    except:
        abort(404)
        #redirect(url_for(account.invalid_token))

    form = SetPasswordForm()
    if form.validate_on_submit():
        try:
            email = ts.loads(form.token.data, salt=secret, max_age=86400)
        except:
            abort(404)
        user = User.query.filter_by(email=form.email.data).first()
        if (user and user.is_not_banned() and email == user.email)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            user.authenticated=True
            login_user(user, remember=True)
            return redirect(url_for("home.index"))
    return render_template("account/set_password.html",form=form)

@mod.route('/account/signin',methods=['GET','POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if (user
            and user.is_not_banned()
            and user.password_is_correct(form.password.data) ):
            #store the authentcation state for login_user to access
            user.authenticated=True
            login_user(user, remember=True)
            return redirect(url_for("home.index"))
    flash("invalid email or password")
    return render_template("account/signin.html",form=form)


#@login_required
def logout():
    logout_user()
    return render_template("home/index.html")




