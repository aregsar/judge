from flask import Blueprint,render_template
mod = Blueprint('home',__name__)



@mod.route('/')
def index():
    #1/0
    #return 'home.index'
    return render_template("home/index.html")

