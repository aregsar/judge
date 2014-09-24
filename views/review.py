from flask import Blueprint,render_template,g,request,redirect,url_for
from flask.ext.login import current_user,LoginManager,login_required,login_user,logout_user
from plugins import db
from models.judgereview import JudgeReview
from models.judge import Judge
from models.user import User
from forms.review.add_review_form import AddReviewForm
from forms.review.edit_review_form import EditReviewForm
from forms.review.edit_review_admin_form import EditReviewAdminForm

mod = Blueprint('review',__name__)

@mod.route('/user/<id>/reviews')
@login_required
#def user(id):
def reviewer(id):
    user = User.query.get(id)
    if user == None:
        return render_template("user/notfound.html")
    reviews = JudgeReview.query.filter_by(reviewer_id=id).all()
    return render_template("review/indexbyuser.html",reviews=reviews,user=user)

@mod.route('/judge/<id>/reviews')
@login_required
def index(id):
    judge = Judge.query.get(id)
    if judge == None:
        return render_template("judge/notfound.html")
    reviews = JudgeReview.query.filter_by(judge_id=id).all()
    return render_template("review/index.html",reviews=reviews,judge=judge)

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
            review = JudgeReview(title=form.title.data,
                                body=form.body.data,
                                rating= form.rating.data,
                                judge_id = judge.id,
                                judge_name = judge.name,
                                #judge= judge,
                                #current_user=current_user
                                reviewer_id = current_user.id,
                                reviewer_name = current_user.username)
            db.session.add(review)
            db.session.commit()
            return redirect(url_for('review.index',id=judge.id))
        return render_template("review/add.html",form=form,id=id)
    else:
        return redirect(url_for('review.edit',id=review.id))

@mod.route('/review/<id>')
@login_required
def review(id):
    review = JudgeReview.query.get(id)
    if review == None:
        return render_template("review/notfound.html")
    return render_template("review/review.html",review=review)


@mod.route('/review/<id>/edit',methods=['GET','POST'])
@login_required
def edit(id):
    review = JudgeReview.query.get(id)
    if review == None:
        return render_template("review/notfound.html")
    if current_user.id == review.reviewer_id or current_user.user_role == "admin":
        if current_user.user_role == "admin":
            form = EditReviewAdminForm(title=review.title,
                                       body=review.body,
                                       active = review.active,
                                       removed = review.removed,
                                       rating=review.rating)
            if form.validate_on_submit():
                review.body = form.body.data
                review.title = form.title.data
                review.rating = form.rating.data
                review.active = form.active.data
                review.removed = form.removed.data
                db.session.commit()
                return redirect(url_for('review.review',id=review.id))
            return render_template("review/editadmin.html",form=form,id=review.id)
            # form = EditReviewForm(title=review.title,body=review.body,rating=review.rating)
            # return render_template("review/edit.html",form=form,id=review.id)
        else:
            form = EditReviewForm(title=review.title,body=review.body,rating=review.rating)
            if form.validate_on_submit():
                review.body = form.body.data
                review.title = form.title.data
                review.rating = form.rating.data
                db.session.commit()
                return redirect(url_for('review.review',id=review.id))
            return render_template("review/edit.html",form=form,id=review.id)
    return "forbidden" #abort(403)
