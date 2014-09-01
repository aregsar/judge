from flask import Blueprint,render_template,g
mod = Blueprint('home',__name__)

#uncomment for blueprint specific error handler
#@mod.app_errorhandler(404)
#def not_found(e):
    #return render_template("home/404.html")


@mod.route('/')
def index():
    #1/0
    #return 'home.index'
    #abort(404)
    print g.current_user
    return render_template("home/index.html")

