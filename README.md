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

===========
app

-total_reviews = Reviews.GetCount()

-total_judges

-total_users

-average_reviews_per_judge

-average_reviews_per_user


Review.addReview(judge, reviewer, overal_rating ,isuues_rating ,decourum_rating)

{

average_rating = (overal_rating + isuues_rating + decourum_rating) \ 3

db.Add(review)

db.commit()

}

==============

http://css-tricks.com/css-sprites-with-inline-images/

.clip               { position: absolute; top: 0; left: 0; }
.pos-1              { clip:rect(0 48px 48px 0); }
<img src="images/arrow-sprite.png" alt="arrow" class="clip pos-1" />

=============
all positions relative to top or left of the image
clip: rect(top-pos,right-pos,bot-pos,left-pos);


.offscreen{clip:rect(0 0 0 0);position:absolute;left:-9999px;
top:auto;overflow:hidden;width:1px;height:1px}

.star-img{display:block;width:100%;
height:100%;background:url(//s3-media3.ak.yelpcdn.com/assets/2/www/img/
c2252a4cd43e/ico/stars/v2/stars_map.png) no-repeat}

.rating .stars_0{background-position:-3px -3px}
.rating .stars_1{background-position:-3px -21px}
.rating .stars_1_half{background-position:-3px -39px}
.rating .stars_2{background-position:-3px -57px}
.rating .stars_2_half{background-position:-3px -75px}
.rating .stars_3{background-position:-3px -93px}
.rating .stars_3_half{background-position:-3px -111px}
.rating .stars_4{background-position:-3px -129px}
.rating .stars_4_half{background-position:-3px -147px}
.rating .stars_5{background-position:-3px -165px}
.rating-small{float:left;position:relative;overflow:hidden;width:49px;height:9px}.rating-small
.stars_0{background-position:-3px -183px}
.rating-small .stars_1{background-position:-3px -195px}.rating-small .stars_1_half{background-position:-3px -207px}.rating-small .stars_2{background-position:-3px -219px}.rating-small .stars_2_half{background-position:-3px -231px}.rating-small .stars_3{background-position:-3px -243px}.rating-small .stars_3_half{background-position:-3px -255px}.rating-small .stars_4{background-position:-3px -267px}.rating-small .stars_4_half{background-position:-3px -279px}.rating-small .stars_5{background-position:-3px -291px}
.rating-large{overflow:hidden;position:relative;width:106px;height:18px}
.rating-large .stars_0{background-position:-3px -303px}.rating-large .stars_1{background-position:-3px -324px}
.rating-large
.stars_1_half{background-position:-3px -345px}.rating-large .stars_2{background-position:-3px -366px}.rating-large .stars_2_half{background-position:-3px -387px}.rating-large .stars_3{background-position:-3px -408px}.rating-large .stars_3_half{background-position:-3px -429px}.rating-large .stars_4{background-position:-3px -450px}.rating-large .stars_4_half{background-position:-3px -471px}.rating-large .stars_5{background-position:-3px -492px}.rating-very-large{overflow:hidden;position:relative;width:126px;height:22px}.rating-very-large
.stars_0{background-position:-3px -514px}.rating-very-large .stars_1{background-position:-3px -539px}.rating-very-large .stars_1_half{background-position:-3px -564px}.rating-very-large .stars_2{background-position:-3px -589px}.rating-very-large .stars_2_half{background-position:-3px -614px}.rating-very-large .stars_3{background-position:-3px -639px}.rating-very-large .stars_3_half{background-position:-3px -664px}.rating-very-large .stars_4{background-position:-3px -689px}.rating-very-large .stars_4_half{background-position:-3px -714px}.rating-very-large .stars_5{background-position:-3px -739px}

<div class="rating">
<i class="star-img stars_4" title="4.0 star rating">
<img alt="4.0 star rating" class="offscreen"
height="303" src="http://s3-media3.fl.yelpcdn.com/assets/2/www/img/
c2252a4cd43e/ico/stars/v2/stars_map.png" width="84">
</i>
</div>






@media print{
.star-img{position:absolute;background:none;width:auto;height:auto}
.star-img img{position:relative;top:0;left:-3px;width:auto;height:auto}
.rating .stars_0{top:-3px}
.rating .stars_1{top:-21px}
.rating .stars_1_half{top:-39px}
.rating .stars_2{top:-57px}
.rating .stars_2_half{top:-75px}
.rating .stars_3{top:-93px}
.rating .stars_3_half{top:-111px}
.rating .stars_4{top:-129px}
.rating .stars_4_half{top:-147px}
.rating .stars_5{top:-165px}
.rating-small .stars_0{top:-183px}
.rating-small .stars_1{top:-195px}
.rating-small .stars_1_half{top:-207px}
.rating-small .stars_2{top:-219px}
.rating-small .stars_2_half{top:-231px}
.rating-small .stars_3{top:-243px}
.rating-small .stars_3_half{top:-255px}
.rating-small .stars_4{top:-267px}
.rating-small .stars_4_half{top:-279px}
.rating-small .stars_5{top:-291px}
.rating-large .stars_0{top:-303px}
.rating-large .stars_1{top:-324px}
.rating-large .stars_1_half{top:-345px}
.rating-large .stars_2{top:-366px}
.rating-large .stars_2_half{top:-387px}
.rating-large .stars_3{top:-408px}
.rating-large .stars_3_half{top:-429px}
.rating-large .stars_4{top:-450px}
.rating-large .stars_4_half{top:-471px}
.rating-large .stars_5{top:-492px}
.rating-very-large .stars_0{top:-514px}
.rating-very-large .stars_1{top:-539px}
.rating-very-large .stars_1_half{top:-564px}
.rating-very-large .stars_2{top:-589px}
.rating-very-large .stars_2_half{top:-614px}
.rating-very-large .stars_3{top:-639px}
.rating-very-large .stars_3_half{top:-664px}
.rating-very-large .stars_4{top:-689px}
.rating-very-large .stars_4_half{top:-714px}
.rating-very-large .stars_5{top:-739px}
}

====================

