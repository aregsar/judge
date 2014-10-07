from flask import Blueprint,render_template,g, current_app
from flask.ext.login import current_user
#NameError: global name 'SigninForm' is not defined
#from forms.account import signin_form
from forms.account.signin_form import SigninForm
from forms.judge.judge_search_form import JudgeSearchForm



#this bluprint is registered in blueprints.py
mod = Blueprint('home',__name__)


#uncomment for blueprint specific error handler
#@mod.app_errorhandler(404)
#def not_found(e):
    #return render_template("home/404.html")


@mod.route('/')
def index():
    #print current_user
    #1/0
    #return 'home.index'
    #abort(404)
    #print g.current_user

    # dump users
    # from models.user import User
    # from sqlalchemy.engine import create_engine
    # from sqlalchemy.sql import select
    # engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
    # connection = engine.connect()
    # s = select([User.__table__])
    # result = connection.execute(s)
    # print result.fetchall()
    # connection.close()

    # connection = engine.connect()
    # result = connection.execute("select username from users")
    # for row in result:
    #   print "username:", row['username']
    # connection.close()

    #using session
    #session.query(User).update({"email": "a@g.com"})
    #result = session.execute("select * from table where id=:id", {'id':7})
    #result = session.execute(select([mytable]).where(mytable.c.id==7))


    if current_user.is_authenticated():
        form = JudgeSearchForm()
        return render_template("home/dashboard.html",form=form)
    else:
        #must pass an empty form for antiXSS
        form = SigninForm()
        return render_template("home/index.html",form=form)


@mod.route('/dashboard')
def dashboard():
    return render_template("home/dashboard.html")

