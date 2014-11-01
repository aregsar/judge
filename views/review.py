from flask import Blueprint,render_template,g,request,redirect,url_for, current_app
from flask.ext.login import current_user,LoginManager,login_required,login_user,logout_user
from plugins import db
from forms.review.add_review_form import AddReviewForm
from forms.review.edit_review_form import EditReviewForm
from forms.review.edit_review_admin_form import EditReviewAdminForm
from models.judgereview import JudgeReview
from models.judge import Judge
from models.user import User

mod = Blueprint('review',__name__)

def can_get_pending_reviews(db_user):
    if db_user.id == current_user.id or current_user.user_role == "admin":
        return True
    return False

def can_view_review(review):
    if review.reviewer_id == current_user.id or current_user.user_role == "admin":
        return True
    if review.active and not review.removed:
        return True
    return False


def can_edit_review(review):
    if current_user.user_role == "admin":
        return True
    if review.active == False  and current_user.id == review.reviewer_id:
        return True
    return False


@mod.route('/reviews/pending')
@login_required
def pending():
    reviews = []
    if current_user.user_role == "admin":
        reviews = JudgeReview.query.filter_by(active=False).all()
    return render_template("review/pending.html",reviews=reviews)

@mod.route('/user/<id>/reviews')
@login_required
#def user(id):
def reviewer(id):
    user = User.query.get(id)
    if user == None:
        return render_template("user/notfound.html")
    if can_get_pending_reviews(user):
        reviews = JudgeReview.query.filter_by(reviewer_id=id).all()
    else:
        reviews = JudgeReview.query.filter_by(reviewer_id=id,active=True).all()
    return render_template("review/indexbyuser.html",reviews=reviews,user=user)

@mod.route('/judge/<id>/reviews')
@login_required
def index(id):
    judge = Judge.query.get(id)
    if judge == None:
        return render_template("judge/notfound.html")
    reviews = JudgeReview.query.filter_by(judge_id=id,active=True).order_by(JudgeReview.id.desc()).limit(20).all()
    return render_template("review/index.html",reviews=reviews,judge=judge)

#TODO:ajax load more
@mod.route('/judge/<id>/reviews/<last_review_id>')
@login_required
def more(id):
    judge = Judge.query.get(id)
    if judge == None:
        return render_template("judge/notfound.html")
    #reviews = JudgeReview.query.filter_by(judge_id=id,active=True).filter(JudgeReview.id > last_review_id).order_by(JudgeReview.id.desc()).limit(20).all()
    reviews = []
    return render_template("review/index.html",reviews=reviews)

@mod.route('/review/<id>')
@login_required
def review(id):
    review = JudgeReview.query.get(id)
    if review == None:
        return render_template("review/notfound.html")
    reviewer = User.query.get(review.reviewer_id)
    if reviewer == None:
        return render_template("review/notfound.html")
    judge = Jude.query.get(review.judge_id)
    if judge == None:
        return render_template("review/notfound.html")
    can_show_edit_review_link = True
    if review.active:
        can_show_edit_review_link= False
    if can_view_review(review):
        return render_template("review/review.html",judge=judge, reviewer = reviewer, review=review,can_show_edit_review_link=can_show_edit_review_link)
    return "forbidden" #abort(403)



@mod.route('/judge/<id>/review/add',methods=['GET','POST'])
@login_required
def add(id):
    judge = Judge.query.get(id)
    if judge == None:
        return render_template("judge/notfound.html")
    review = JudgeReview.query.filter_by(judge_id=id,reviewer_id=current_user.id).first()
    if review == None:
        form = AddReviewForm()
        if form.validate_on_submit():
            review = JudgeReview(
                                body=form.body.data,
                                rating= int(form.rating.data),
                                knowledge= int(form.knowledge.data),
                                decorum= int(form.decorum.data),
                                tentatives= int(form.tentatives.data),
                                curiosity= int(form.curiosity.data),
                                judge_id = judge.id,
                                judge_name = judge.name,
                                #judge= judge,
                                #current_user=current_user
                                reviewer_id = current_user.id,
                                reviewer_name = current_user.username)
            review.add_rating_averages(judge, current_user)
            db.session.add(review)
            db.session.commit()
            #return redirect(url_for('review.index',id=judge.id))
            #return redirect(url_for('review.reviewer',id=current_user.id))
            return redirect(url_for('review.index',id=id))
        return render_template("review/add.html",form=form,judge=judge)
    else:
        if review.active:
            if can_view_review(review):
                return redirect(url_for('review.review',id=review.id))
            return "forbidden" #abort(403)
        else:
            return redirect(url_for('review.edit',id=review.id))



# @mod.route('/review/<id>/report',methods=['GET','POST'])
# @login_required
# def report(id):
#     if request.method == 'POST':
#         review = JudgeReview.query.get(id)
#         review.flagged = True
#         review.flagger_id = current_user.id
#         db.session.commit()
#         return render_template("review/reported.html")
#     return render_template("review/report.html",id=id)




@mod.route('/review/<id>/edit',methods=['GET','POST'])
@login_required
def edit(id):
    review = JudgeReview.query.get(id)
    if review == None:
        return render_template("review/notfound.html")
    #if current_user.id == review.reviewer_id or current_user.user_role == "admin":
    if can_edit_review(review):
        if current_user.user_role == "admin":
            form = EditReviewAdminForm(
                                        body=review.body,
                                        rating= str(review.rating),
                                        knowledge= str(review.knowledge),
                                        decorum= str(review.decorum),
                                        tentatives= str(review.tentatives),
                                        curiosity= str(review.curiosity),
                                        active = review.active,
                                        removed = review.removed)
            if form.validate_on_submit():
                review.body = form.body.data
                review.rating= int(form.rating.data)
                review.knowledge= int(form.knowledge.data)
                review.decorum= int(form.decorum.data)
                review.tentatives= int(form.tentatives.data)
                review.curiosity= int(form.curiosity.data)
                if current_user.user_role == "admin":
                    review.active = form.active.data
                    review.removed = form.removed.data
                db.session.commit()
                return redirect(url_for('review.review',id=review.id))
            return render_template("review/editadmin.html",form=form,review=review)
            # form = EditReviewForm(title=review.title,body=review.body,rating=review.rating)
            # return render_template("review/edit.html",form=form,id=review.id)
        else:
            form = EditReviewForm(
                                    body=review.body,
                                    knowledge= str(review.knowledge),
                                    decorum= str(review.decorum),
                                    tentatives= str(review.tentatives),
                                    curiosity= str(review.curiosity),
                                    rating=str(review.rating))
            if form.validate_on_submit():
                review.body = form.body.data
                review.rating= int(form.rating.data)
                review.knowledge= int(form.knowledge.data)
                review.decorum= int(form.decorum.data)
                review.tentatives= int(form.tentatives.data)
                review.curiosity= int(form.curiosity.data)
                db.session.commit()
                return redirect(url_for('review.review',id=review.id))
            return render_template("review/edit.html",form=form,review=review)
    return "forbidden" #abort(403)
