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
from models.userjudge import UserJudge

#this bluprint is registered in blueprints.py
mod = Blueprint('judge',__name__)



@mod.route('/judge/tracked')
@login_required
def tracked():
    judges= UserJudge.query.all()
    return render_template("judge/tracked.html",judges=judges)


@mod.route('/judge/track')
@login_required
def track():
    return render_template("judge/track.html")

@mod.route('/judge/untrack')
@login_required
def untrack():
    return render_template("judge/untrack.html")

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
    #form = JudgeSubmitForm(judge_name=name)
    form = JudgeSubmitForm()
    print "submit"
    if form.validate_on_submit():
        print "submit valid"
        judge = Candidate(
                name=form.judge_name.data.strip())
        db.session.add(judge)
        db.session.commit()
        return render_template("judge/submitted.html")
    form.judge_name.data = name
    return render_template("judge/submit.html",form=form,name=name)



@mod.route('/judge/add',methods=['GET','POST'])
@login_required
def add():
    if current_user.user_role != "admin":
        return render_template("judge/notfound.html")
    form = JudgeEditForm()
    if form.validate_on_submit():
        print "submitted"
        #judge = Judge(name=form.name.data)
        #judge = CreateActiveJudge(form.name.data,"CA","court","district",scope=1)
        judge = Judge(form.name.data.strip(),
                       form.state.data.strip(),
                       int(form.scope.data))#works without int conversion
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
        #judge = CreateRetiredJudge(form.name.data,"CA",scope="Arbitrator")
        judge = Judge(form.name.data.strip(),
                       form.state.data.strip(),
                       int(form.scope.data),#works without int conversion
                       retired=True)
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
        #form = RetiredJudgeEditForm(name=judge.name,scope=judge.scope,state=judge.state)
        if form.validate_on_submit():
            judge.name = form.name.data.strip()
            judge.state = form.state.data.strip()
            judge.scope = int(form.scope.data)#works without int conversion
            db.session.commit()
            #return redirect(url_for('judge.edit',id=id))
            return redirect(url_for('judge.profile',id=id))
        form.name.data = judge.name
        form.state.data = judge.state
        form.scope.data = str(judge.scope)#does not work without string conversion
        return render_template("judge/editretired.html",form=form,id=id)
    else:
        form = JudgeEditForm()
        #form = JudgeEditForm(name=judge.name,scope=judge.scope,state=judge.state)
        if form.validate_on_submit():
            judge.name = form.name.data.strip()
            judge.state = form.state.data.strip()
            judge.scope = int(form.scope.data)#works without int conversion
            db.session.commit()
            #return redirect(url_for('judge.edit',id=id))
            return redirect(url_for('judge.profile',id=id))
        form.name.data = judge.name
        form.state.data = judge.state
        form.scope.data = str(judge.scope)#does not work without string conversion
        return render_template("judge/edit.html",form=form,id=id)



