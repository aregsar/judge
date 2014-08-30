from flask import Blueprint,render_template
#home = Blueprint('home',__name__)
mod = Blueprint('home',__name__)



#@mod.route('/')
def index():
    #1/0
    return 'home.index'

