judge
=====

[
    {"keys": ["f5"], "command": "refresh_folder_list" }
]

cmd-opt / #to comment or uncomment blocks and lines
(venv)$ pip install -r requirements.txt
(venv)$ pip freeze > requirements.txt

realpython discover flask part 9 sqlalchemy
around 16 minute mark there is discussion around avoiding circular imports

==========
#using flask-uuid
#@app.route('/<uuid(strict=False):id>'>
#@app.route('/<uuid:id>')
#def mypage(id):
#    return id  # 'id' is a uuid.UUID instance
#import uuid
#url_for('mypage', id=uuid.uuid4())

===========
import os
os.urandom(24)

SECRET_KEY='\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD'

app.secret_key = '\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD'

===========
export secretkey='\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD'

DEBUG=os.environ['JUDGE_DEBUG']
SECRET_KEY=os.environ['JUDGE_SECRET_KEY']
SQLALCHEMY_DATABASE_URL=os.environ['DATABASE_URL']
========
app.database #sqlite database file
app.config['SQLALCHEMY_DATABASE_URL']='postgres://xxxxx/yyyyy'

#need to manually create database before running sqlalchemy create_db.py ???
$ pgstart
$ psql
aregsarkissian=# CREATE DATABASE judgedb;

in create_db.py file
#from app import db
from plugins import db
from models import User
db.create_all()

#from the shell
#create (database specified with SQLALCHEMY_DATABASE_URL???)
#and create users table
$python db_create.py
--------------

if request.method == 'POST':
request.form['username']
errormessage=None
return render_template("aa.html",errormessage=errormessage)
session['name']= "abcd"
session.pop('username',None)
if 'name' in session:
flash('username or password invalid')
{% for message in get_flashed_messages() %}
{{message}}
{% endfor %}

{% if errormessage %}
{{errormessage}}
{% endif %}

<input type="text" name="email" value="{{ request.form.email }}">

def Signin():
g.db = connect_db()
g.db.close()
-------------------------------------


Setting up a new Flask project

(note always create a README.md file when creating a new repo on github)

a-Create a new Flask project from by cloning a new github repo called myapp

#go to flask projects directory
$ cd ~/flaskprojects

#clone the new repo
$ git clone git@github.com:aregsar/myapp.git

#create a .gitignore file in the project directory
$ cd myapp
$ touch .gitignore

# open modify and save .gitignore file with sublime
$ subl .gitignore

#add following lines to .gitignore and save
*.pyc
*.pyo
env
env*
dist
*.egg
*.egg-info

#create virtual environment directory venv in the project directory
$ virtualenv -p $(which python) venv

#activate the virtual directory
$ . venv/bin/activate

#install flask
(venv)$ pip install flask==0.10.1

#create the requirements.txt file with the current flask version
(venv)$ pip freeze > requirements.txt

(venv)$ subl requirements.txt

#add to requirements.txt the lines below:
flask-script
flask-sqlalchemy
flask-login
flask-wtf

(venv)$ pip install -r requirements.txt
(venv)$ pip freeze > requirements.txt

#commit remote and local changes
$git pull origin master
$git add .
$git commit -m “committed”

#push commits to github branch
$git push origin master

#deactivate virtual environment
(venv)$deactivate

——————————————————————————————————————————————————————

b-Create a new Flask project locally and push it to a new github repo  called myapp

#go to flask projects directory
$ cd ~/flaskprojects

#create a new flask project
$ mkdir myapp
$ cd myapp

# create a local git repo
$ git init
# set the origin for this project to point to your new empty gthub repo
$ git remote add origin git@github.com:aregsar/myapp.git

#create a .gitignore file
$ touch .gitignore

# open modify and save .gitignore file with sublime
$ subl .gitignore

#add following lines to .gitignore and save

#get the path for python 2.7
#$ export PYTHON_HOME=$(which python)
#$ echo $PYTHON_HOME
#$ which python
/usr/local/bin/python

#create virtual environment directory venv in the project directory
#$ virtualenv -p $PYTHON_HOME venv
#$ virtualenv -p /usr/local/bin/python venv
$ virtualenv -p $(which python) venv

# activate the virtual directory
$ . venv/bin/activate

(venv)$ pip install flask

#create the requirements.txt file with the current flask version
(venv)$ pip freeze > requirements.txt

(venv)$ subl requirements.txt

#add to requirements.txt the lines below:
flask-script
flask-sqlalchemy
flask-login
flask-wtf

(venv)$ pip install -r requirements.txt
(venv)$ pip freeze > requirements.txt

#commit remote and local changes
$git add .
$git commit -m “committed”
$git pull origin master

#push commits to github branch
$git push origin master

#deactivate virtual environment
(venv)$deactivate

=================

Flask==0.10.1
Flask-Login==0.2.11
Flask-SQLAlchemy==1.0
Flask-Script==2.0.5
Flask-WTF==0.10.1
Jinja2==2.7.3
MarkupSafe==0.23
SQLAlchemy==0.9.7
WTForms==2.0.1
Werkzeug==0.9.6
itsdangerous==0.24
wsgiref==0.1.2

