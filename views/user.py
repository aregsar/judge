from flask import Blueprint,render_template,g,request,redirect,url_for, current_app
from flask.ext.login import current_user,LoginManager,login_required,login_user,logout_user
from plugins import db
from forms.user.edit_user_admin_form import EditUserAdminForm
from models.user import User

mod = Blueprint('user',__name__)


@mod.route('/user')
@login_required
def index():
    users= User.query.all()
    return render_template("user/index.html",users=users)

@mod.route('/user/<id>')
@login_required
def profile(id):
    judge_id = request.args.get('judge')
    user = User.query.get(id)
    if user == None:
        return render_template("user/notfound.html")
    return render_template("user/profile.html",user=user,judge_id=judge_id)


@mod.route('/user/edit/<id>',methods=['GET','POST'])
@login_required
def edit(id):
    if current_user.user_role != "admin":
        return render_template("user/notfound.html")
    user = User.query.get(id)
    if user == None:
        return render_template("user/notfound.html")
    form = EditUserAdminForm(banned=user.banned)
    if form.validate_on_submit():
        #user.banned = form.banned.data
        if form.banned.data == True:
            user.ban()
        else:
            user.unban()
        db.session.commit()
        #return redirect(url_for('judge.edit',id=id))
        return redirect(url_for('user.profile',id=id))
    return render_template("user/edit.html",form=form,user=user)
