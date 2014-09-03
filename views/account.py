from flask import Blueprint,render_template,g
mod = Blueprint('account',__name__)



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
    #return redirect(url_for("home.index"))
    #return redirect(url_for("home.dashboard"))
    return render_template("account/signup.html")
