from flask import Blueprint,render_template,g,request,abort,redirect,url_for, current_app
from flask.ext.login import current_user,LoginManager,login_required,login_user,logout_user
from plugins import db
#from forms.account.signin_form import SigninForm
from forms.judge.judge_search_form import JudgeSearchForm
from forms.judge.judge_submit_form import JudgeSubmitForm
from forms.judge.judge_edit_form import JudgeEditForm
from forms.judge.retired_judge_edit_form import RetiredJudgeEditForm
from models.judge import Judge, CreateRetiredJudge,CreateActiveJudge
from models.candidate import Candidate

#this bluprint is registered in blueprints.py
mod = Blueprint('judge',__name__)


@mod.route('/judge/sitting')
@login_required
def sitting():
    judges= Judge.query.filter_by(retired=False).all()
    return render_template("judge/sitting.html",judges=judges)

@mod.route('/judge/retired')
@login_required
def retired():
    judges= Judge.query.filter_by(retired=True).all()
    return render_template("judge/retired.html",judges=judges)


@mod.route('/judge')
@login_required
def index():
    name = request.args.get('name')
    form = JudgeSearchForm(name=name)
    judges= Judge.query.filter_by(name=name).all()
    message = None
    if len(judges) == 0:
        message = "Didn't find your judge? Submit them for review by clicking here."
    return render_template("judge/index.html",form=form,judges=judges,name=name,
                           message=message)

@mod.route('/judge/candidates')
@login_required
def candidates():
    if current_user.user_role == "admin":
        judges = Candidate.query.all()
        return render_template("judge/candidates.html",judges=judges)
    abort(404)




@mod.route('/judge/submit/<name>',methods=['GET','POST'])
@login_required
def submit(name):
    form = JudgeSubmitForm(name=name)
    if form.validate_on_submit():
        judge = Candidate(name=name)
        db.session.add(judge)
        db.session.commit()
        return render_template("judge/submitted.html")
    return render_template("judge/submit.html",form=form,name=name)



@mod.route('/judge/add',methods=['GET','POST'])
@login_required
def add():
    if current_user.user_role != "admin":
        return render_template("judge/notfound.html")
    form = JudgeEditForm()
    if form.validate_on_submit():
        #judge = Judge(name=form.name.data)
        judge = CreateActiveJudge(form.name.data,"CA","court","district",scope="State")
        db.session.add(judge)
        db.session.commit()
        return redirect(url_for('judge.profile',id=judge.id))
        #return redirect(url_for('judge.edit',id=judge.id))
        #form.name.data = judge.name
        #return render_template("judge/edit.html",form=form,id=judge.id)
    return render_template("judge/add.html",form=form)

@mod.route('/judge/add/retired',methods=['GET','POST'])
@login_required
def addretired():
    if current_user.user_role != "admin":
        return render_template("judge/notfound.html")
    form = RetiredJudgeEditForm()
    if form.validate_on_submit():
        judge = CreateRetiredJudge(form.name.data,"CA",scope="Arbitrator")
        db.session.add(judge)
        db.session.commit()
        return redirect(url_for('judge.profile',id=judge.id))
        #return redirect(url_for('judge.edit',id=judge.id))
        #form.name.data = judge.name
        #return render_template("judge/editretired.html",form=form,id=judge.id)
    return render_template("judge/addretired.html",form=form)


@mod.route('/judge/<id>')
@login_required
def profile(id):
    judge = Judge.query.get(id)
    if judge == None:
        return render_template("judge/notfound.html")
    #can_show_add_review_link = False;
    can_show_edit_judge_link = False;
    if current_user.user_role == "admin":
        can_show_edit_judge_link = True
    return render_template("judge/profile.html",judge=judge,can_show_edit_judge_link=can_show_edit_judge_link)

@mod.route('/judge/<id>/edit',methods=['GET','POST'])
@login_required
def edit(id):
    if current_user.user_role != "admin":
        return render_template("judge/notfound.html")
    judge = Judge.query.get(id)
    if judge == None:
        return render_template("judge/notfound.html")
    if judge.retired:
        form = RetiredJudgeEditForm()
        #form = RetiredJudgeEditForm(name=judge.name)
        if form.validate_on_submit():
            judge.name = form.name.data
            #judge.scope = form.scope.data
            db.session.commit()
            #return redirect(url_for('judge.edit',id=id))
            return redirect(url_for('judge.profile',id=id))
        form.name.data = judge.name
        return render_template("judge/editretired.html",form=form,id=id)
    else:
        form = JudgeEditForm()
        #form = JudgeEditForm(name=judge.name)
        if form.validate_on_submit():
            judge.name = form.name.data
            #judge.scope = form.scope.data
            #judge.district = form.district.data
            #judge.court = form.court.data
            db.session.commit()
            #return redirect(url_for('judge.edit',id=id))
            return redirect(url_for('judge.profile',id=id))
        form.name.data = judge.name
        return render_template("judge/edit.html",form=form,id=id)



