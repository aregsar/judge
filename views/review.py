from flask import Blueprint,render_template,g,request
from forms.review.add_review_form import AddReviewForm
from flask.ext.login import current_user
from forms.judge_search_form import JudgeSearchForm
from flask.ext.login import LoginManager,login_required,login_user,logout_user
from plugins import db
from models.judgereview import JudgeReview

mod = Blueprint('review',__name__)


@mod.route('/judge/<id>/reviews')
@login_required
def index(id):
    #return "judge reviews " + id
    reviews= JudgeReview.query.filter_by(judge_id=id).all()
    return render_template("review/index.html",reviews=reviews)

@mod.route('/judge/<id>/review/add')
@login_required
def add(id):
    #return "judge add review " + id
    return render_template("review/add.html")

@mod.route('/review/<id>')
@login_required
def review(id):
    #return "review " + id
    return render_template("review/review.html")


@mod.route('/review/<id>/edit')
@login_required
def edit(id):
    #return "judge edit review " + id
    return render_template("review/edit.html")
