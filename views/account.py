from flask import Blueprint,render_template,g
mod = Blueprint('account',__name__)


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

@mod.route('/account/confirm')
def confirm():
    return render_template("account/account_confirmed.html")

@mod.route('/account/confirm',methods=['POST'])
def confirm():
    if False;
        return redirect(url_for("home.dashboard"))
    return render_template("account/account_confirmation_error.html")

