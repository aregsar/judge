import sys
from flask import Blueprint,redirect, render_template, url_for, g, current_app,flash
import uuid
from plugins import db, flaskuuid,bcrypt
#NameError: global name 'SigninForm' is not defined
#from forms import signin_form, signup_form, forgotpassword_form
from forms.signin_form import SigninForm
from forms.signup_form import SignupForm
from forms.forgotpassword_form import ForgotPasswordForm
from itsdangerous import URLSafeTimedSerializer
from flask.ext.login import LoginManager,login_required,login_user,logout_user
#from models import user
from models.user import User

mod = Blueprint('account',__name__)

@mod.route('/account/signup',methods=['GET','POST'])
def signup():
    #print current_app.name
    form = SignupForm()
    if form.validate_on_submit():
        print "signup valid"
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash("account with email exists.")
            return render_template("account/signup.html",form=form)
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash("username taken, please try another.")
            return render_template("account/signup.html",form=form)
        user = User.query.filter_by(barnumber=form.barnumber.data).first()
        if user:
            flash("account with bar number exists.")
            return render_template("account/signup.html",form=form)
        email = form.email.data
        secret = current_app.config["SECRET_KEY"]
        ts = URLSafeTimedSerializer(secret)
        token = ts.dumps(email, salt=secret)
        confirm_url = url_for('account.confirm',token=token,_external=True)

        user = User(
            email = email,
            password = form.password.data,
            barnumber=form.barnumber.data,
            username=form.username.data)
        try:
            db.session.add(user)
            db.session.commit()
        except: #sqlalchemy.exc.IntegrityError
            #need to also catch unique constraint violations and display validation errors
            #e = sys.exc_info()[0]
            #flash("Error: %s" % e)
            flash("There was an error while creating your account.")
            flash("Please try resubmitting the form again.")
            flash("If the error persits please try again in a few minutes")
            flash("You can always check for updates to the status of our website on twitter.com\judgejungle")
            return render_template("account/signup.html",form=form)
        try:

            html_email = render_template('account/confirmation_email.html',confirm_url=confirm_url)
            #html = render_template('account/created.html')

            #set up a test only view to display the email. link to it from account/created.html
            confirmation_email_url = url_for('account.confirmation_email',token=token,_external=True)
            html = render_template('account/created.html',confirmation_email_url=confirmation_email_url)
            #

            #subject = "JudgeJungle account activation email"
            #send_email(email, subject, html_email)
            return html
        except:
            #e = sys.exc_info()[0]
            #flash("Error: %s" % e)
            flash("Signup was success but there was an error sending the confirmation email.")
            #redirect(url_for("account.error_signup_email_delivery"))
    return render_template("account/signup.html",form=form)

#this route if for testing only. It is a confirmation email short circuit loopback
@mod.route('/account/confirmation_email/<token>')
def confirmation_email(token):
    confirm_url = url_for('account.confirm',token=token,_external=True)
    return render_template('account/confirmation_email.html',confirm_url=confirm_url)


@mod.route('/account/confirm/<token>')
def confirm(token):
    secret = current_app.config["SECRET_KEY"]
    ts = URLSafeTimedSerializer(secret)
    try:
        email = ts.loads(token, salt=secret, max_age=86400)
        user = User.query.filter_by(email=email).first()
    except:
        return render_template("account/confirmation_failed.html")

    #print user.activated

    try:
        user.activate()
        db.session.commit()
    except:
        #flash("There was an error while confirming your account.")
        #flash("Please try the confirmation link again.")
        #flash("If the error persits please try the confirmation link again. in a few minutes")
        #flash("You can always check for updates to the status of our website on twitter.com\judgejungle")
        return render_template("account/confirmation_error.html")


    user = User.query.filter_by(email=email).first()
    #print user.activated
    form = SigninForm(email=email)

    # #return redirect(url_for('account.signin'))
    # flash("Account verified. Please sign in")
    return render_template("account/confirm.html",form=form)


@mod.route('/account/signin',methods=['GET','POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        #if (user and not user.is_banned() ):
        if user:
            # #if user.password_is_correct(form.password.data):
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.refresh_signin_token_and_date()
                db.session.commit()
                #store the authentcation state for login_user to access
                user.authenticated=True
                login_user(user, remember=True)
                return redirect(url_for("home.index"))
    flash("invalid email or password")
    return render_template("account/signin.html",form=form)


@login_required
def logout():
    logout_user()
    return render_template("home/index.html")




@mod.route('/account/password/activate',methods=['GET','POST'])
def forgot_password():
    secret = current_app.config["SECRET_KEY"]
    ts = URLSafeTimedSerializer(secret)
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first_or_404()
        if user.is_not_banned():
            token = ts.dumps(self.email, salt=secret)
        if user.activated:
            password_url = url_for('account.reset_password',token=token,_external=True)
            #html = render_template('account/reset_password.html',password_url=password_url)
            return render_template("account/reset_password.html",password_url=password_url)
        else:
            confirm_url = url_for('account.confirm',token=token,_external=True)
            #html = render_template('account/confirm.html',confirm_url=confirm_url)
            return render_template("account/confirm.html",confirm_url=confirm_url)
    return render_template("account/forgot_password.html",form=form)


@mod.route('/account/password/reset/<token>')
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
    secret = current_app.config["SECRET_KEY"]
    ts = URLSafeTimedSerializer(secret)
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
        if (user and user.is_not_banned() and email == user.email):
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            user.authenticated=True
            login_user(user, remember=True)
            return redirect(url_for("home.index"))
    return render_template("account/set_password.html",form=form)






