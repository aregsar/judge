from flask import Blueprint,render_template,g,request,abort,redirect,url_for
from forms.signin_form import SigninForm
from flask.ext.login import current_user
from forms.judge_search_form import JudgeSearchForm
from forms.judge_submit_form import JudgeSubmitForm
from forms.judge_edit_form import JudgeEditForm
from forms.retired_judge_edit_form import RetiredJudgeEditForm
from flask.ext.login import LoginManager,login_required,login_user,logout_user
from plugins import db
from models.judge import Judge, CreateRetiredJudge,CreateActiveJudge
from models.candidate import Candidate
#this bluprint is registered in blueprints.py
mod = Blueprint('judge',__name__)




@mod.route('/judge')
@login_required
def index():
    #if current_user.is_authenticated():
    name = request.args.get('name')
    form = JudgeSearchForm(name=name)
    judges= Judge.query.filter_by(name=name).all()
    message = None
    if len(judges) == 0:
        message = "Didn't find your judge? Submit them for review by clicking here."
    return render_template("judge/index.html",form=form,judges=judges,name=name,message=message)

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
    form = JudgeEditForm()
    if form.validate_on_submit():
        #judge = Judge(name=form.name.data)
        judge = CreateActiveJudge(form.name.data,"CA","court","district",scope="State")
        db.session.add(judge)
        db.session.commit()
        return redirect(url_for('judge.edit',id=judge.id))
        #form.name.data = judge.name
        #return render_template("judge/edit.html",form=form,id=judge.id)
    return render_template("judge/add.html",form=form)

@mod.route('/judge/add/retired',methods=['GET','POST'])
@login_required
def addretired():
    form = RetiredJudgeEditForm()
    if form.validate_on_submit():
        #judge = Judge(name=form.name.data,retired=True)
        judge = CreateRetiredJudge(form.name.data,"CA",scope="Arbitrator")
        db.session.add(judge)
        db.session.commit()
        return redirect(url_for('judge.edit',id=judge.id))
        #form.name.data = judge.name
        #return render_template("judge/editretired.html",form=form,id=judge.id)
    return render_template("judge/addretired.html",form=form)

@mod.route('/judge/edit/<id>',methods=['GET','POST'])
@login_required
def edit(id):
    judge = Judge.query.get(id)
    if judge == None:
        abort(404)
    if judge.retired:
        form = RetiredJudgeEditForm()
        if form.validate_on_submit():
            judge.name = form.name.data
            #judge.scope = form.scope.data
            db.session.commit()
            return redirect(url_for('judge.edit',id=id))
        form.name.data = judge.name
        return render_template("judge/editretired.html",form=form,id=id)
    else:
        form = JudgeEditForm()
        if form.validate_on_submit():
            judge.name = form.name.data
            #judge.scope = form.scope.data
            #judge.district = form.district.data
            #judge.court = form.court.data
            db.session.commit()
            return redirect(url_for('judge.edit',id=id))
        form.name.data = judge.name
        return render_template("judge/edit.html",form=form,id=id)



