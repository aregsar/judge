import sys
import uuid
from itsdangerous import URLSafeTimedSerializer
from flask import Blueprint,redirect, render_template, url_for, g, current_app,flash
from flask.ext.login import LoginManager,login_required,login_user,logout_user,current_user
from plugins import db, flaskuuid,bcrypt
#NameError: global name 'SigninForm' is not defined
#from forms.account import signin_form, signup_form, forgotpassword_form
from forms.account.signin_form import SigninForm
from forms.account.signup_form import SignupForm
from forms.account.forgotpassword_form import ForgotPasswordForm
#from models import user
from models.user import User

#this bluprint is registered in blueprints.py
mod = Blueprint('account',__name__)

@mod.route('/account/signup',methods=['GET','POST'])
def signup():
    #print current_app.name
    form = SignupForm()
    if form.validate_on_submit():
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
        user = User(
            email = form.email.data.strip(),
            password = form.password.data.strip(),
            barnumber = form.barnumber.data.strip(),
            username = form.username.data.strip(),
            firstname = form.firstname.data.strip(),
            lastname = form.lastname.data.strip(),
            state = form.state.data.strip())

        user.refresh_signin_token_and_date()

        try:

            db.session.add(user)
            db.session.commit()
        except: #sqlalchemy.exc.IntegrityError
            #need to also catch unique constraint violations and display validation errors
            #e = sys.exc_info()[0]
            #flash("Error: %s" % e)
            flash("There was an error while creating your account.")
            return render_template("account/signup.html",form=form)
        try:
            #store the authentcation state for login_user
            #to access via user.is_authenticated()
            user.authenticated=True
            #login_user uses user.is_authenticated() and user.is_active()
            login_user(user, remember=True)
            return redirect(url_for("home.index"))
            #return render_template('account/created.html',confirmation_email_url='#')

        except:
            #e = sys.exc_info()[0]
            #flash("Error: %s" % e)
            flash("Signup was success but there was an error sending the confirmation email.")
            #redirect(url_for("account.error_signup_email_delivery"))
    return render_template("account/signup.html",form=form)


@mod.route('/account/signin',methods=['GET','POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.strip()).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data.strip()):
                user.refresh_signin_token_and_date()
                db.session.commit()
                #store the authentcation state for login_user
                #to access via user.is_authenticated()
                user.authenticated=True
                #login_user uses user.is_authenticated() and user.is_active()
                login_user(user, remember=True)
                return redirect(url_for("home.index"))
    flash("invalid email or password")
    return render_template("account/signin.html",form=form)


#@login_required
@mod.route('/account/signout')
def signout():
    logout_user()
    return redirect(url_for("home.index"))


@mod.route('/account/password',methods=['GET','POST'])
def set_password():
    pass

# @mod.route('/account/pending')
# @login_required
# def pending():
#     accounts = []
#     if current_user.user_role == "admin":
#         users = User.query.filter_by(approved=False).all()
#         return render_template("account/pending.html",users=users)
#     return "forbidden"



# @mod.route('/account/approve/<id>')
# @login_required
# def approve(id):
#     if current_user.user_role == "admin":
#         user = User.query.get(id)
#         if user:
#             secret = current_app.config["SECRET_KEY"]
#             ts = URLSafeTimedSerializer(secret)
#             token = ts.dumps(user.email, salt=secret)
#             confirm_url = url_for('account.confirm',token=token,_external=True)
#             html_email = render_template('account/confirmation_email.html',confirm_url=confirm_url)
#             try:
#                 user.approve()
#                 db.session.commit()
#             except:
#                 return render_template("account/confirmation_error.html")
#             #subject = "JudgeJungle account activation email"
#             #send_email(email, subject, html_email)
#         else:
#             return "not found"
#     else:
#         return "forbidden"
#     return redirect(url_for("account.pending"))


# @mod.route('/account/signup',methods=['GET','POST'])
# def signup():
#     #print current_app.name
#     form = SignupForm()
#     if form.validate_on_submit():
#         print "signup valid"
#         user = User.query.filter_by(email=form.email.data).first()
#         if user:
#             flash("account with email exists.")
#             return render_template("account/signup.html",form=form)
#         user = User.query.filter_by(username=form.username.data).first()
#         if user:
#             flash("username taken, please try another.")
#             return render_template("account/signup.html",form=form)
#         user = User.query.filter_by(barnumber=form.barnumber.data).first()
#         if user:
#             flash("account with bar number exists.")
#             return render_template("account/signup.html",form=form)
#         email = form.email.data.strip()
#         secret = current_app.config["SECRET_KEY"]
#         ts = URLSafeTimedSerializer(secret)
#         token = ts.dumps(email, salt=secret)
#         confirm_url = url_for('account.confirm',token=token,_external=True)

#         user = User(
#             email = email.strip(),
#             password = form.password.data.strip(),
#             barnumber = form.barnumber.data.strip(),
#             username = form.username.data.strip(),
#             firstname = form.firstname.data.strip(),
#             lastname = form.lastname.data.strip(),
#             state = form.state.data.strip())
#         try:
#             db.session.add(user)
#             db.session.commit()
#         except: #sqlalchemy.exc.IntegrityError
#             #need to also catch unique constraint violations and display validation errors
#             #e = sys.exc_info()[0]
#             #flash("Error: %s" % e)
#             flash("There was an error while creating your account.")
#             return render_template("account/signup.html",form=form)
#         try:

#             html_email = render_template('account/confirmation_email.html',confirm_url=confirm_url)
#             #html = render_template('account/created.html')

#             #set up a test only view to display the email. link to it from account/created.html
#             confirmation_email_url = url_for('account.confirmation_email',token=token,_external=True)
#             html = render_template('account/created.html',confirmation_email_url=confirmation_email_url)

#             #subject = "JudgeJungle account activation email"
#             #send_email(email, subject, html_email)
#             return html
#         except:
#             #e = sys.exc_info()[0]
#             #flash("Error: %s" % e)
#             flash("Signup was success but there was an error sending the confirmation email.")
#             #redirect(url_for("account.error_signup_email_delivery"))
#     return render_template("account/signup.html",form=form)

#this route if for testing only. It is a confirmation email short circuit loopback
# @mod.route('/account/confirmation_email/<token>')
# def confirmation_email(token):
#     confirm_url = url_for('account.confirm',token=token,_external=True)
#     return render_template('account/confirmation_email.html',confirm_url=confirm_url)


# @mod.route('/account/confirm/<token>')
# def confirm(token):
#     secret = current_app.config["SECRET_KEY"]
#     ts = URLSafeTimedSerializer(secret)
#     try:
#         email = ts.loads(token, salt=secret, max_age=86400)
#         user = User.query.filter_by(email=email).first()
#     except:
#         return render_template("account/confirmation_failed.html")

#     try:
#         user.activate()
#         db.session.commit()
#     except:
#         #flash("There was an error while confirming your account.")
#         return render_template("account/confirmation_error.html")
#     form = SigninForm(email=email)
#     return render_template("account/confirm.html",form=form)




@mod.route('/account/password/activate',methods=['GET','POST'])
def forgot_password():
    pass
#     secret = current_app.config["SECRET_KEY"]
#     ts = URLSafeTimedSerializer(secret)
#     form = ForgotPasswordForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data.strip()).first_or_404()
#         if user.is_not_banned():
#             token = ts.dumps(self.email, salt=secret)
#         if user.activated:
#             password_url = url_for('account.reset_password',token=token,_external=True)
#             #html = render_template('account/reset_password.html',password_url=password_url)
#             return render_template("account/reset_password.html",password_url=password_url)
#         else:
#             confirm_url = url_for('account.confirm',token=token,_external=True)
#             #html = render_template('account/confirm.html',confirm_url=confirm_url)
#             return render_template("account/confirm.html",confirm_url=confirm_url)
#     return render_template("account/forgot_password.html",form=form)


# @mod.route('/account/password/reset/<token>')
# def reset_password(token):
#     try:
#         email = ts.loads(token, salt=secret, max_age=86400)
#     except:
#         abort(404)
#         #redirect(url_for(account.invalid_token))

#     form = SetPasswordForm()
#     #form.token.data = token
#     return render_template("account/set_password.html",form=form,token=token)

# @mod.route('/account/password/set/<token>',methods=['GET','POST'])
# def set_password(token):
#     secret = current_app.config["SECRET_KEY"]
#     ts = URLSafeTimedSerializer(secret)
#     try:
#         email = ts.loads(token, salt=secret, max_age=86400)
#     except:
#         abort(404)
#         #redirect(url_for(account.invalid_token))

#     form = SetPasswordForm()
#     if form.validate_on_submit():
#         try:
#             email = ts.loads(form.token.data, salt=secret, max_age=86400)
#         except:
#             abort(404)
#         user = User.query.filter_by(email=form.email.data.strip()).first()
#         if (user and user.is_not_banned() and email == user.email):
#             user.set_password(form.password.data.strip())
#             db.session.add(user)
#             db.session.commit()
#             user.authenticated=True
#             login_user(user, remember=True)
#             return redirect(url_for("home.index"))
#     return render_template("account/set_password.html",form=form)






