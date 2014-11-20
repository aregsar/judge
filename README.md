judge
=====
162f9fbd31bdd3dc539a66fd8a8c7ea2e0c5a0bb
commit one
f143f92b197ef34dc6013d2e5280b7b5bdc05bec
commit two



Python ideaoms:
print '%s,%i,%c'.format(name,age,sex)
print '{},{},{}'.format(name,age,sex)
print '{name},{age},{sex}'.format(name=name,age=age,sex=sex)
print '{user.name},{user.age},{user.sex}'.format(user=user)

print ''.join(['a','b','c'])
print ','.join(['a','b','c'])
print ''.join('a','b','c') #not sure if this works

book = book.strip().upper().replace(':',',')

for index,book in enumerate(books):
    print str(index)

def dictfunc(*args,**kwargs):
    pass

=======

[
    {"keys": ["f5"], "command": "refresh_folder_list" }
]
=============
GUNICORN

#running the project using gunicorn at localhost:4000
$ gunicorn -b 127.0.0.1:4000 app:judgeapp



HEROKU

http://judgejungle.herokuapp.com/


git push heroku master
Permission denied (publickey)
#solution is to execute
$ heroku keys:add



#project proc file contains
web: gunicorn app:judgeapp
#where judgeapp is set in app.py:
judgeapp = create_app()

#run localhost:5000 flask server using heroku config settings in .env file
$ foreman start

$ heroku config:set JUDGE_DEBUG=False
$ heroku config:set JUDGE_ENV=PROD
$ heroku config:set JUDGE_SECRET_KEY='\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD'




#show heroku app status
$ heroku ps
$ heroku ps:scale web=1
$ heroku run python createdb.py

Preparing static assets
Collectstatic configuration error. To debug, run:
$ heroku run python ./manage.py collectstatic --noinput



#the .env file in project is only used locally by foreman

#show heroku app configuaration
$ heroku config
$ heroku config:get
$ heroku config:set
$ heroku config:unset

DATABASE_URL:               postgres://bnrdvdaaqshbvl:FeO9CfI4hk3MfPGw4rSRNkMSua@ec2-54-83-199-115.compute-1.amazonaws.com:5432/dfdvvpcbvta6f2
HEROKU_POSTGRESQL_JADE_URL: postgres://jsxsbzqcfhuzcw:OfDZfU0VcgrmFrLTxS2Vy9Kuav@ec2-54-204-38-16.compute-1.amazonaws.com:5432/dcmo0m39l5mh3r
HEROKU_POSTGRESQL_ONYX_URL: postgres://bnrdvdaaqshbvl:FeO9CfI4hk3MfPGw4rSRNkMSua@ec2-54-83-199-115.compute-1.amazonaws.com:5432/dfdvvpcbvta6f2

$ heroku config:set FLASK_DEBUG=False
$ heroku config:set FLASK_ENVIRONMENT=PROD
$ heroku config:set SECRET_KEY='\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD'

$ heroku run python createdb.py

========================

cmd-opt / #to comment or uncomment blocks and lines
(venv)$ pip install -r requirements.txt
(venv)$ pip freeze > requirements.txt

realpython discover flask part 9 sqlalchemy
around 16 minute mark there is discussion around avoiding circular imports

=======================
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

    #use session
    #session.query(User).update({"email": "a@g.com"})
    #result = session.execute("select * from table where id=:id", {'id':7})
    #result = session.execute(select([mytable]).where(mytable.c.id==7))

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

all positions relative to top or left of the image
clip: rect(top-pos,right-pos,bot-pos,left-pos);

http://css-tricks.com/css-sprites-with-inline-images/

.clip{
position: absolute;
top: 0;
left: 0;
}

.pos-1{
clip:rect(0 48px 48px 0);
}

<div class="rating">
<img src="images/arrow-sprite.png" alt="arrow" class="clip pos-1" />
</div>

.rating        { position: relative; height: 15px; width: 84px; }
=============



.offscreen{
clip:rect(0 0 0 0);
position:absolute;
left:-9999px;
top:auto;
overflow:hidden;
width:1px;
height:1px
}

.stars_0{
background-position:-3px -3px
}

.star-img{
display:block;
width:100%;
height:100%;
background:url(//s3-media3....../v2/stars_map.png) no-repeat
}

<i class="star-img stars_0">
<img class="offscreen"
height="303"  width="84" src="http://s3-media3....../v2/stars_map.png">
</i>




===================


.offscreen{clip:rect(0 0 0 0);position:absolute;left:-9999px;
top:auto;overflow:hidden;width:1px;height:1px}

.star-img{display:block;width:100%;
height:100%;background:url(//s3-media3.ak.yelpcdn.com/assets/2/www/img/
c2252a4cd43e/ico/stars/v2/stars_map.png) no-repeat}

.rating{position:relative;overflow:hidden;width:84px;height:18px}
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
.rating-small{float:left;position:relative;overflow:hidden;width:49px;height:9px}
.rating-small .stars_0{background-position:-3px -183px}
.rating-small .stars_1{background-position:-3px -195px}
.rating-small .stars_1_half{background-position:-3px -207px}
.rating-small .stars_2{background-position:-3px -219px}
.rating-small .stars_2_half{background-position:-3px -231px}
.rating-small .stars_3{background-position:-3px -243px}
.rating-small .stars_3_half{background-position:-3px -255px}
.rating-small .stars_4{background-position:-3px -267px}
.rating-small .stars_4_half{background-position:-3px -279px}
.rating-small .stars_5{background-position:-3px -291px}
.rating-large{overflow:hidden;position:relative;width:106px;height:18px}
.rating-large .stars_0{background-position:-3px -303px}
.rating-large .stars_1{background-position:-3px -324px}
.rating-large .stars_1_half{background-position:-3px -345px}
.rating-large .stars_2{background-position:-3px -366px}
.rating-large .stars_2_half{background-position:-3px -387px}
.rating-large .stars_3{background-position:-3px -408px}
.rating-large .stars_3_half{background-position:-3px -429px}
.rating-large .stars_4{background-position:-3px -450px}
.rating-large .stars_4_half{background-position:-3px -471px}
.rating-large .stars_5{background-position:-3px -492px}
.rating-very-large{overflow:hidden;position:relative;width:126px;height:22px}
.rating-very-large .stars_0{background-position:-3px -514px}
.rating-very-large .stars_1{background-position:-3px -539px}
.rating-very-large .stars_1_half{background-position:-3px -564px}
.rating-very-large .stars_2{background-position:-3px -589px}
.rating-very-large .stars_2_half{background-position:-3px -614px}
.rating-very-large .stars_3{background-position:-3px -639px}
.rating-very-large .stars_3_half{background-position:-3px -664px}
.rating-very-large .stars_4{background-position:-3px -689px}
.rating-very-large .stars_4_half{background-position:-3px -714px}
.rating-very-large .stars_5{background-position:-3px -739px}



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
#interactive cli
pip install ipython

#export your .xlsx to a .csv file
import csv
with open('file.csv','rb') as file:
    contents = csv.reader(file)
    matrix = list()
    for row in contents:
        matrix.append(row)

matrix.pop(0)
#for row in matrix:
for index,row in enumerate(matrix):
    judgeid = row[0]
    print judgeid



#access F13 with matrix[5][12]
print matrix[0]
print matrix[1]
print matrix[2246]
print matrix[0][0]
print matrix[0][1]
print matrix[1][0]
print matrix[1][1]


===========================

['Judge Identification Number',
 'Judge Last Name',
 'Judge First Name',
 'Judge Middle Name',
 'Suffix',
 'Birth month',
 'Birth day',
 'Birth year',
 'Place of Birth (City)',
 'Place of Birth (State)',
 'Death month',
 'Death day',
 'Death year',
 'Place of Death (City)',
 'Place of Death (State)',
 'Gender',
 'Race or Ethnicity',
 'Judge Identification Number',
 'Court Name',
 'Court Type',
 'President name',
 'Party Affiliation of President',
 'Renominating President name',
 'Party Affiliation of Renominating President',
 'Nomination Date Senate Executive Journal',
 'ABA Rating',
 'Recess Appointment date',
 'Vice last name (predecessor)',
 'Vice first name (predecessor)',
 'Authorization legislation',
 'Referral date (referral to Judicial Committee)',
 'Report number',
 'Committee action',
 'Committee action date',
 'Hearings',
 'Senate voice vote',
 'Senate vote Ayes/Nays',
 'Senate Vote Date (Confirmation Date)',
 'Commission Date',
 'Commission Year',
 'Date of Service as Chief Judge (begin)',
 'Date of Service as Chief Judge (end)',
 'Second Date of Service as Chief Judge (begin)',
 'Second Date of Service as Chief Judge (end)',
 'Retirement from Active Service',
 'Date of Termination',
 'Termination specific reason',
 'Judge Identification Number',
 'Court Name (2)',
 'Court Type (2)',
 'President name (2)',
 'Party Affiliation of President (2)',
 'Renominating President name (2)',
 'Party Affiliation of Renominating President (2)',
 'Nomination Date Senate Executive Journal (2)',
 'ABA Rating (2)',
 'Recess Appointment date (2)',
 'Vice last name (predecessor) (2)',
 'Vice first name (predecessor) (2)',
 'Authorization legislation (2)',
 'referral date (referral to Judicial Committee) (2)',
 'Report number (2)',
 'committee action (2)',
 'Committee action date (2)',
 'Hearings (2)',
 'Senate voice vote (2)',
 'Senate vote Ayes/Nays (2)',
 'Senate Vote Date (Confirmation Date) (2)',
 'Commission Date (2)',
 'Date of Service as Chief Judge (begin) (2)',
 'Date of Service as Chief Judge (end) (2)',
 'Second Date of Service as Chief Judge (begin) (2)',
 'Second Date of Service as Chief Judge (end) (2)',
 'Retirement from Active Service (2)',
 'Date of Termination (2)',
 'Termination specific reason (2)',
 'Judge Identification Number',
 'Court Name (3)',
 'Court Type (3)',
 'President name (3)',
 'Party Affiliation of President (3)',
 'Renominating President name (3)',
 'Party Affiliation of Renominating President (3)',
 'Nomination Date Senate Executive Journal (3)',
 'ABA Rating (3)',
 'Recess Appointment date (3)',
 'Vice last name (predecessor) (3)',
 'Vice first name (predecessor) (3)',
 'Authorization legislation (3)',
 'referral date (referral to Judicial Committee) (3)',
 'Report number (3)',
 'committee action (3)',
 'Committee action date (3)',
 'Hearings (3)',
 'Senate voice vote (3)',
 'Senate vote Ayes/Nays (3)',
 'Senate Vote Date (Confirmation Date) (3)',
 'Commission Date (3)',
 'Date of Service as Chief Judge (begin) (3)',
 'Date of Service as Chief Judge (end) (3)',
 'Second Date of Service as Chief Judge (begin) (3)',
 'Second Date of Service as Chief Judge (end) (3)',
 'Retirement from Active Service (3)',
 'Date of Termination (3)',
 'Termination specific reason (3)',
 'Judge Identification Number',
 'Court Name (4)',
 'Court Type (4)',
 'President name (4)',
 'Party Affiliation of President (4)',
 'Renominating President name (4)',
 'Party Affiliation of Renominating President (4)',
 'Nomination Date Senate Executive Journal (4)',
 'ABA Rating (4)',
 'Recess Appointment date (4)',
 'Vice last name (predecessor) (4)',
 'Vice first name (predecessor) (4)',
 'Authorization legislation (4)',
 'referral date (referral to Judicial Committee) (4)',
 'Report number (4)',
 'committee action (4)',
 'Committee action date (4)',
 'Hearings (4)',
 'Senate voice vote (4)',
 'Senate vote Ayes/Nays (4)',
 'Senate Vote Date (Confirmation Date) (4)',
 'Commission Date (4)',
 'Date of Service as Chief Judge (begin) (4)',
 'Date of Service as Chief Judge (end) (4)',
 'Second Date of Service as Chief Judge (begin) (4)',
 'Second Date of Service as Chief Judge (end) (4)',
 'Retirement from Active Service (4)',
 'Date of Termination (4)',
 'Termination specific reason (4)',
 'Judge Identification Number',
 'Court Name (5)',
 'Court Type (5)',
 'President name (5)',
 'Party Affiliation of President (5)',
 'Renominating President name (5)',
 'Party Affiliation of Renominating President (5)',
 'Nomination Date Senate Executive Journal (5)',
 'ABA Rating (5)',
 'Recess Appointment date (5)',
 'Vice last name (predecessor) (5)',
 'Vice first name (predecessor) (5)',
 'Authorization legislation (5)',
 'referral date (referral to Judicial Committee) (5)',
 'Report number (5)',
 'committee action (5)',
 'Committee action date (5)',
 'Hearings (5)',
 'Senate voice vote (5)',
 'Senate vote Ayes/Nays (5)',
 'Senate Vote Date (Confirmation Date) (5)',
 'Commission Date (5)',
 'Date of Service as Chief Judge (begin) (5)',
 'Date of Service as Chief Judge (end) (5)',
 'Second Date of Service as Chief Judge (begin) (5)',
 'Second Date of Service as Chief Judge (end) (5)',
 'Retirement from Active Service (5)',
 'Date of Termination (5)',
 'Termination specific reason (5)',
 'Judge Identification Number',
 'Court Name (6)',
 'Court Type (6)',
 'President name (6)',
 'Party Affiliation of President (6)',
 'Nomination Date Senate Executive Journal (6)',
 'Renominating President name (6)',
 'Party Affiliation of Renominating President (6)',
 'ABA Rating (6)',
 'Recess Appointment date (6)',
 'Vice last name (predecessor) (6)',
 'Vice first name (predecessor) (6)',
 'Authorization legislation (6)',
 'referral date (referral to Judicial Committee) (6)',
 'Report number (6)',
 'committee action (6)',
 'Committee action date (6)',
 'Hearings (6)',
 'Senate voice vote (6)',
 'Senate vote Ayes/Nays (6)',
 'Senate Vote Date (Confirmation Date) (6)',
 'Commission Date (6)',
 'Date of Service as Chief Judge (begin) (6)',
 'Date of Service as Chief Judge (end) (6)',
 'Second Date of Service as Chief Judge (begin) (6)',
 'Second Date of Service as Chief Judge (end) (6)',
 'Retirement from Active Service (6)',
 'Date of Termination (6)',
 'Termination specific reason (6)',
 'Name of School',
 'Degree',
 'Degree year',
 'Name of School (2)',
 'Degree (2)',
 'Degree year (2)',
 'Name of School (3)',
 'Degree (3)',
 'Degree year (3)',
 'Name of School (4)',
 'Degree (4)',
 'Degree year (4)',
 'Name of School (5)',
 'Degree  (5)',
 'Degree year (5)',
 'Employment text field',
 'Bankruptcy and Magistrate service']






===========================================
===========================================
===========================================








'Judge Identification Number',
 'Judge Last Name',
 'Judge First Name',
 'Judge Middle Name',
 'Suffix',
 'Birth month',
 'Birth day',
 'Birth year',
 'Place of Birth (City)',
 'Place of Birth (State)',
 'Death month',
 'Death day',
 'Death year',
 'Place of Death (City)',
 'Place of Death (State)',
 'Gender',
 'Race or Ethnicity',
 'Judge Identification Number',
 'Court Name',
 'Court Type',
 'President name',
 'Party Affiliation of President',
 'Renominating President name',
 'Party Affiliation of Renominating President',
 'Nomination Date Senate Executive Journal',
 'ABA Rating',
 'Recess Appointment date',
 'Vice last name (predecessor)',
 'Vice first name (predecessor)',
 'Authorization legislation',
 'Referral date (referral to Judicial Committee)',
 'Report number',
 'Committee action',
 'Committee action date',
 'Hearings',
 'Senate voice vote',
 'Senate vote Ayes/Nays',
 'Senate Vote Date (Confirmation Date)',
 'Commission Date',
 'Commission Year',
 'Date of Service as Chief Judge (begin)',
 'Date of Service as Chief Judge (end)',
 'Second Date of Service as Chief Judge (begin)',
 'Second Date of Service as Chief Judge (end)',
 'Retirement from Active Service',
 'Date of Termination',
 'Termination specific reason',
 'Judge Identification Number',
 'Court Name (2)',
 'Court Type (2)',
 'President name (2)',
 'Party Affiliation of President (2)',
 'Renominating President name (2)',
 'Party Affiliation of Renominating President (2)',
 'Nomination Date Senate Executive Journal (2)',
 'ABA Rating (2)',
 'Recess Appointment date (2)',
 'Vice last name (predecessor) (2)',
 'Vice first name (predecessor) (2)',
 'Authorization legislation (2)',
 'referral date (referral to Judicial Committee) (2)',
 'Report number (2)',
 'committee action (2)',
 'Committee action date (2)',
 'Hearings (2)',
 'Senate voice vote (2)',
 'Senate vote Ayes/Nays (2)',
 'Senate Vote Date (Confirmation Date) (2)',
 'Commission Date (2)',
 'Date of Service as Chief Judge (begin) (2)',
 'Date of Service as Chief Judge (end) (2)',
 'Second Date of Service as Chief Judge (begin) (2)',
 'Second Date of Service as Chief Judge (end) (2)',
 'Retirement from Active Service (2)',
 'Date of Termination (2)',
 'Termination specific reason (2)',
 'Judge Identification Number',
 'Court Name (3)',
 'Court Type (3)',
 'President name (3)',
 'Party Affiliation of President (3)',
 'Renominating President name (3)',
 'Party Affiliation of Renominating President (3)',
 'Nomination Date Senate Executive Journal (3)',
 'ABA Rating (3)',
 'Recess Appointment date (3)',
 'Vice last name (predecessor) (3)',
 'Vice first name (predecessor) (3)',
 'Authorization legislation (3)',
 'referral date (referral to Judicial Committee) (3)',
 'Report number (3)',
 'committee action (3)',
 'Committee action date (3)',
 'Hearings (3)',
 'Senate voice vote (3)',
 'Senate vote Ayes/Nays (3)',
 'Senate Vote Date (Confirmation Date) (3)',
 'Commission Date (3)',
 'Date of Service as Chief Judge (begin) (3)',
 'Date of Service as Chief Judge (end) (3)',
 'Second Date of Service as Chief Judge (begin) (3)',
 'Second Date of Service as Chief Judge (end) (3)',
 'Retirement from Active Service (3)',
 'Date of Termination (3)',
 'Termination specific reason (3)',
 'Judge Identification Number',
 'Court Name (4)',
 'Court Type (4)',
 'President name (4)',
 'Party Affiliation of President (4)',
 'Renominating President name (4)',
 'Party Affiliation of Renominating President (4)',
 'Nomination Date Senate Executive Journal (4)',
 'ABA Rating (4)',
 'Recess Appointment date (4)',
 'Vice last name (predecessor) (4)',
 'Vice first name (predecessor) (4)',
 'Authorization legislation (4)',
 'referral date (referral to Judicial Committee) (4)',
 'Report number (4)',
 'committee action (4)',
 'Committee action date (4)',
 'Hearings (4)',
 'Senate voice vote (4)',
 'Senate vote Ayes/Nays (4)',
 'Senate Vote Date (Confirmation Date) (4)',
 'Commission Date (4)',
 'Date of Service as Chief Judge (begin) (4)',
 'Date of Service as Chief Judge (end) (4)',
 'Second Date of Service as Chief Judge (begin) (4)',
 'Second Date of Service as Chief Judge (end) (4)',
 'Retirement from Active Service (4)',
 'Date of Termination (4)',
 'Termination specific reason (4)',
 'Judge Identification Number',
 'Court Name (5)',
 'Court Type (5)',
 'President name (5)',
 'Party Affiliation of President (5)',
 'Renominating President name (5)',
 'Party Affiliation of Renominating President (5)',
 'Nomination Date Senate Executive Journal (5)',
 'ABA Rating (5)',
 'Recess Appointment date (5)',
 'Vice last name (predecessor) (5)',
 'Vice first name (predecessor) (5)',
 'Authorization legislation (5)',
 'referral date (referral to Judicial Committee) (5)',
 'Report number (5)',
 'committee action (5)',
 'Committee action date (5)',
 'Hearings (5)',
 'Senate voice vote (5)',
 'Senate vote Ayes/Nays (5)',
 'Senate Vote Date (Confirmation Date) (5)',
 'Commission Date (5)',
 'Date of Service as Chief Judge (begin) (5)',
 'Date of Service as Chief Judge (end) (5)',
 'Second Date of Service as Chief Judge (begin) (5)',
 'Second Date of Service as Chief Judge (end) (5)',
 'Retirement from Active Service (5)',
 'Date of Termination (5)',
 'Termination specific reason (5)',
 'Judge Identification Number',
 'Court Name (6)',
 'Court Type (6)',
 'President name (6)',
 'Party Affiliation of President (6)',
 'Nomination Date Senate Executive Journal (6)',
 'Renominating President name (6)',
 'Party Affiliation of Renominating President (6)',
 'ABA Rating (6)',
 'Recess Appointment date (6)',
 'Vice last name (predecessor) (6)',
 'Vice first name (predecessor) (6)',
 'Authorization legislation (6)',
 'referral date (referral to Judicial Committee) (6)',
 'Report number (6)',
 'committee action (6)',
 'Committee action date (6)',
 'Hearings (6)',
 'Senate voice vote (6)',
 'Senate vote Ayes/Nays (6)',
 'Senate Vote Date (Confirmation Date) (6)',
 'Commission Date (6)',
 'Date of Service as Chief Judge (begin) (6)',
 'Date of Service as Chief Judge (end) (6)',
 'Second Date of Service as Chief Judge (begin) (6)',
 'Second Date of Service as Chief Judge (end) (6)',
 'Retirement from Active Service (6)',
 'Date of Termination (6)',
 'Termination specific reason (6)',
 'Name of School',
 'Degree',
 'Degree year',
 'Name of School (2)',
 'Degree (2)',
 'Degree year (2)',
 'Name of School (3)',
 'Degree (3)',
 'Degree year (3)',
 'Name of School (4)',
 'Degree (4)',
 'Degree year (4)',
 'Name of School (5)',
 'Degree  (5)',
 'Degree year (5)',
 'Employment text field',
 'Bankruptcy and Magistrate service']

=======================
import pandas as pd
xl = pd.ExcelFile(path + filename)
xl.sheet_names

>>> [u'Sheet1', u'Sheet2', u'Sheet3']

df = xl.parse("Sheet1")
df.head()
======================
import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("pytest.xls")
sheet = book.sheet_by_name("source")
numcolumns = sheet.ncols
numrows = sheet.nrows
columns = str(sheet.ncols)
rows = str(sheet.nrows)

for r in range(1, numrows):
      product      = sheet.cell(r,).value
      customer = sheet.cell(r,1).value
      rep          = sheet.cell(r,2).value
      date     = sheet.cell(r,3).value
      actual       = sheet.cell(r,4).value
      expected = sheet.cell(r,5).value
      open        = sheet.cell(r,6).value
      closed       = sheet.cell(r,7).value
      city     = sheet.cell(r,8).value
      state        = sheet.cell(r,9).value
      zip         = sheet.cell(r,10).value
      pop          = sheet.cell(r,11).value
      region   = sheet.cell(r,12).value

query = """INSERT INTO orders (product, customer_type, rep, date, actual, expected,
 open_opportunities, closed_opportunities, city, state, zip, population, region) VALUES (%s,
 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

values = (product, customer, rep, date, actual, expected, open, closed, city, state, zip, pop, region)

cursor.execute(query, values)
==========================
#interactive cli
pip install ipython

def add_federal_judges(include,Court_Name_Column):
    for index in include:
        Judge_Identification_Number = matrix[index][0]
        Judge_Last_Name = matrix[index][1]
        Judge_Middle_Name = matrix[index][2]
        Judge_First_Name = matrix[index][3]
        Suffix = matrix[index][4]
        Court_Name = matrix[index][Court_Name_Column]
        #Court_Name = matrix[index][18]
        add_federal_judge(Judge_Identification_Number
        ,Judge_Last_Name,Judge_Middle_Name,Judge_First_Name,Suffix
        ,Court_Name)

def add_federal_judge(Judge_Identification_Number
        ,Judge_Last_Name,Judge_Middle_Name,Judge_First_Name,Suffix
        ,Court_Name):
    pass#

#export your .xlsx to a .csv file
import csv
with open('file.csv','rb') as file:
    contents = csv.reader(file)
    matrix = list()
    for row in contents:
        matrix.append(row)


matrix.pop(0)
include = list()
defered = list()
other = list()
#figure out if a row is in, out or deffered to next pass
for index,row in enumerate(matrix):
    if row[45].trim() == '':
        include.add(index)
    elif(row[45] == 'Reassignment' or
        row[45] == 'Appointment to Another Judicial Position' or
        row[45] == 'Recess Appointment-Not Confirmed' ):
        defered.add(index)
    else:
        other.add(index)

add_federal_judges(include,Couurt_Name_Column=18)

include2 = list()
defered2 = list()
other2 = list()
for index in defered:
    if matrix[index][45].trim() == '':
        include2.add(index)
    elif( matrix[index][74] == 'Reassignment' or
        matrix[index]row[74] == 'Appointment to Another Judicial Position' or
        matrix[index]row[74] == 'Recess Appointment-Not Confirmed' ):
        defered2.add(index)
    else:
        other2.add(index)

add_federal_judges(include2,Couurt_Name_Column=47)

include3 = list()
defered3 = list()
other3 = list()

for index in defered2:
    if matrix[index][103].trim() == '':
        include3.add(index)
    elif( matrix[index][103] == 'Reassignment' or
        matrix[index]row[103] == 'Appointment to Another Judicial Position' or
        matrix[index]row[103] == 'Recess Appointment-Not Confirmed' ):
        defered3.add(index)
    else:
        other3.add(index)

add_federal_judges(include3,Couurt_Name_Column=76)

if len(defered3) > 0:
    print "there is more: " + len(defered3)




#for row in matrix:
for index,row in enumerate(matrix):
    Judge_Identification_Number = row[0]
    Judge Last Name = row[1]
    Judge Middle Name = row[2]
    Judge First Name = row[3]
    Suffix = row[4]
    Judge_Identification_Number_a = row[17]
    Court_Name = row[18]
    Court_Type = row[19]
    Termination_specific_reason  = row[45]
    Judge_Identification_Number_b = row[46]
    Court_Name_2 = row[47]
    Court_Type_2 = row[48]
    Termination_specific_reason_2  = row[74]
    Judge_Identification_Number_c = row[75]
    Court_Name_3 = row[76]
    Court_Type_3 = row[77]
    Termination_specific_reason_3  = row[103]
    Judge_Identification_Number_d = row[104]
    Court_Name_4 = row[105]
    Court_Type_4 = row[106]
    Termination_specific_reason_4  = row[132]
    Judge_Identification_Number_e = row[133]
    Court_Name_5 = row[134]
    Court_Type_5 = row[135]
    Termination_specific_reason_4  = row[161]
    Judge_Identification_Number_f = row[162]
    Court_Name_5 = row[163]
    Court_Type_5 = row[164]
    judgeids = '%i,%i,%i,%i,%i,%i,%i,%i'.format(Judge_Identification_Number_a,
        Judge_Identification_Number_b,
        Judge_Identification_Number_c,
        Judge_Identification_Number_d,
        Judge_Identification_Number_e,
        Judge_Identification_Number_f
    )
    print judgeids




#access F13 with matrix[5][12]
print matrix[0]
print matrix[1]
print matrix[2246]
print matrix[0][0]
print matrix[0][1]
print matrix[1][0]
print matrix[1][1]
==========================
==========================
0 Judge Identification Number
1 Judge Last Name
2 Judge Middle Name
3 Judge First Name
4 Suffix
17 Judge Identification Number
18 Court Name
19 Court Type

45 Termination specific reason <values: (Empty)=>add judge and court name as sitting judge,
[Retirement]=>add as retired judge without court name (for now dont add),
[Death, Resignation,Impeachment & Conviction ]=>remove from list ,
[Reassignment, Appointment to Another Judicial Position, Recess Appointment-Not Confirmed] => defer to next pass
>
46 Judge Identification Number
47 Court Name (2)
48 Court Type (2)

74Termination specific reason (2)
75Judge Identification Number
76 Court Name (3)
77 Court Type (3)

103 Termination specific reason (3)
104 Judge Identification Number
105 Court Name (5)
106 Court Type (5)

132 Termination specific reason (4)
133 Judge Identification Number
134 Court Name (5)
135 Court Type (5)

US State (derived from Court Name based on court type)

==============================
==============================
 0 'Judge Identification Number',
 1 'Judge Last Name',
 2 'Judge First Name',
 3 'Judge Middle Name',
 4 'Suffix',
 'Birth month',
 'Birth day',
 'Birth year',
 'Place of Birth (City)',
 'Place of Birth (State)',
 'Death month',
 'Death day',
 'Death year',
 'Place of Death (City)',
 'Place of Death (State)',
 'Gender',
 'Race or Ethnicity',
 17'Judge Identification Number',
 18 'Court Name',
 19 'Court Type',
 'President name',
 'Party Affiliation of President',
 'Renominating President name',
 'Party Affiliation of Renominating President',
 'Nomination Date Senate Executive Journal',
 'ABA Rating',
 'Recess Appointment date',
 'Vice last name (predecessor)',
 'Vice first name (predecessor)',
 'Authorization legislation',
 'Referral date (referral to Judicial Committee)',
 'Report number',
 'Committee action',
 'Committee action date',
 'Hearings',
 'Senate voice vote',
 'Senate vote Ayes/Nays',
 'Senate Vote Date (Confirmation Date)',
 'Commission Date',
 'Commission Year',
 'Date of Service as Chief Judge (begin)',
 'Date of Service as Chief Judge (end)',
 'Second Date of Service as Chief Judge (begin)',
 'Second Date of Service as Chief Judge (end)',
 'Retirement from Active Service',
 'Date of Termination',
 45'Termination specific reason',
 46'Judge Identification Number',
 47'Court Name (2)',
 48'Court Type (2)',
 'President name (2)',
 'Party Affiliation of President (2)',
 'Renominating President name (2)',
 'Party Affiliation of Renominating President (2)',
 'Nomination Date Senate Executive Journal (2)',
 'ABA Rating (2)',
 'Recess Appointment date (2)',
 'Vice last name (predecessor) (2)',
 'Vice first name (predecessor) (2)',
 'Authorization legislation (2)',
 'referral date (referral to Judicial Committee) (2)',
 'Report number (2)',
 'committee action (2)',
 'Committee action date (2)',
 'Hearings (2)',
 'Senate voice vote (2)',
 'Senate vote Ayes/Nays (2)',
 'Senate Vote Date (Confirmation Date) (2)',
 'Commission Date (2)',
 'Date of Service as Chief Judge (begin) (2)',
 'Date of Service as Chief Judge (end) (2)',
 'Second Date of Service as Chief Judge (begin) (2)',
 'Second Date of Service as Chief Judge (end) (2)',
 'Retirement from Active Service (2)',
 'Date of Termination (2)',
 74 'Termination specific reason (2)',
 75'Judge Identification Number',
 76'Court Name (3)',
 77'Court Type (3)',
 'President name (3)',
 'Party Affiliation of President (3)',
 'Renominating President name (3)',
 'Party Affiliation of Renominating President (3)',
 'Nomination Date Senate Executive Journal (3)',
 'ABA Rating (3)',
 'Recess Appointment date (3)',
 'Vice last name (predecessor) (3)',
 'Vice first name (predecessor) (3)',
 'Authorization legislation (3)',
 'referral date (referral to Judicial Committee) (3)',
 'Report number (3)',
 'committee action (3)',
 'Committee action date (3)',
 'Hearings (3)',
 'Senate voice vote (3)',
 'Senate vote Ayes/Nays (3)',
 'Senate Vote Date (Confirmation Date) (3)',
 'Commission Date (3)',
 'Date of Service as Chief Judge (begin) (3)',
 'Date of Service as Chief Judge (end) (3)',
 'Second Date of Service as Chief Judge (begin) (3)',
 'Second Date of Service as Chief Judge (end) (3)',
 'Retirement from Active Service (3)',
 'Date of Termination (3)',
 103'Termination specific reason (3)',
 104'Judge Identification Number',
 105'Court Name (4)',
 106'Court Type (4)',
 'President name (4)',
 'Party Affiliation of President (4)',
 'Renominating President name (4)',
 'Party Affiliation of Renominating President (4)',
 'Nomination Date Senate Executive Journal (4)',
 'ABA Rating (4)',
 'Recess Appointment date (4)',
 'Vice last name (predecessor) (4)',
 'Vice first name (predecessor) (4)',
 'Authorization legislation (4)',
 'referral date (referral to Judicial Committee) (4)',
 'Report number (4)',
 'committee action (4)',
 'Committee action date (4)',
 'Hearings (4)',
 'Senate voice vote (4)',
 'Senate vote Ayes/Nays (4)',
 'Senate Vote Date (Confirmation Date) (4)',
 'Commission Date (4)',
 'Date of Service as Chief Judge (begin) (4)',
 'Date of Service as Chief Judge (end) (4)',
 'Second Date of Service as Chief Judge (begin) (4)',
 'Second Date of Service as Chief Judge (end) (4)',
 'Retirement from Active Service (4)',
 'Date of Termination (4)',
 132'Termination specific reason (4)',
 133'Judge Identification Number',
 134'Court Name (5)',
 135'Court Type (5)',
 'President name (5)',
 'Party Affiliation of President (5)',
 'Renominating President name (5)',
 'Party Affiliation of Renominating President (5)',
 'Nomination Date Senate Executive Journal (5)',
 'ABA Rating (5)',
 'Recess Appointment date (5)',
 'Vice last name (predecessor) (5)',
 'Vice first name (predecessor) (5)',
 'Authorization legislation (5)',
 'referral date (referral to Judicial Committee) (5)',
 'Report number (5)',
 'committee action (5)',
 'Committee action date (5)',
 'Hearings (5)',
 'Senate voice vote (5)',
 'Senate vote Ayes/Nays (5)',
 'Senate Vote Date (Confirmation Date) (5)',
 'Commission Date (5)',
 'Date of Service as Chief Judge (begin) (5)',
 'Date of Service as Chief Judge (end) (5)',
 'Second Date of Service as Chief Judge (begin) (5)',
 'Second Date of Service as Chief Judge (end) (5)',
 'Retirement from Active Service (5)',
 'Date of Termination (5)',
 161'Termination specific reason (5)',
 162'Judge Identification Number',
 163'Court Name (6)',
 164'Court Type (6)',
 'President name (6)',
 'Party Affiliation of President (6)',
 'Nomination Date Senate Executive Journal (6)',
 'Renominating President name (6)',
 'Party Affiliation of Renominating President (6)',
 'ABA Rating (6)',
 'Recess Appointment date (6)',
 'Vice last name (predecessor) (6)',
 'Vice first name (predecessor) (6)',
 'Authorization legislation (6)',
 'referral date (referral to Judicial Committee) (6)',
 'Report number (6)',
 'committee action (6)',
 'Committee action date (6)',
 'Hearings (6)',
 'Senate voice vote (6)',
 'Senate vote Ayes/Nays (6)',
 'Senate Vote Date (Confirmation Date) (6)',
 'Commission Date (6)',
 'Date of Service as Chief Judge (begin) (6)',
 'Date of Service as Chief Judge (end) (6)',
 'Second Date of Service as Chief Judge (begin) (6)',
 'Second Date of Service as Chief Judge (end) (6)',
 'Retirement from Active Service (6)',
 'Date of Termination (6)',
 'Termination specific reason (6)',
 'Name of School',
 'Degree',
 'Degree year',
 'Name of School (2)',
 'Degree (2)',
 'Degree year (2)',
 'Name of School (3)',
 'Degree (3)',
 'Degree year (3)',
 'Name of School (4)',
 'Degree (4)',
 'Degree year (4)',
 'Name of School (5)',
 'Degree  (5)',
 'Degree year (5)',
 'Employment text field',
 'Bankruptcy and Magistrate service']


==============================

#service oriented coding in an object oriented way
class JudgeData
    #immutable state is only set once at initialization
    def __init__(self,row)
        self.Judge_Identification_Number = row[0]
        self.Judge Last Name = row[1]
        Judge Middle Name = row[2]
        Judge First Name = row[3]
        Suffix = row[4]
        Judge_Identification_Number_a = row[17]
        Court_Name = row[18]
        Court_Type = row[19]
        Termination_specific_reason  = row[45]
        Judge_Identification_Number_b = row[46]
        Court_Name_2 = row[47]
        Court_Type_2 = row[48]
        Termination_specific_reason_2  = row[74]
        Judge_Identification_Number_c = row[75]
        Court_Name_3 = row[76]
        Court_Type_3 = row[77]
        Termination_specific_reason_3  = row[103]
        Judge_Identification_Number_d = row[104]
        Court_Name_4 = row[105]
        Court_Type_4 = row[106]
        Termination_specific_reason_4  = row[132]
        Judge_Identification_Number_e = row[133]
        Court_Name_5 = row[134]
        self.Court_Type_5 = row[135]
        self.Termination_specific_reason_4  = row[161]
        self.Judge_Identification_Number_f = row[162]
        self.Court_Name_5 = row[163]
        self.Court_Type_5 = row[164]

    #query
    #returns result based on internal state, does not change or effect internal state
    def can_add_self_to_database(self)
        #add logic
        return true

    #command
    #changes backing data store, does not change or effect internal state
    def add_self_to_database(self,dbsession)
        pass

    #command executor: executes based on query result
    def add_self_to_database_if_allowed(self,dbsession)
        if(can_add_to_database()):
            add_to_database(dbsession)


    def add_all_allowed_judges_to_database(judgedata_list,dbsession)
        for judgedata in judgedata_list
            judgedata.add_self_to_database_if_allowed(dbsession)



















































































0 'Judge Identification Number',
 1 'Judge Last Name',
 2 'Judge First Name',
 3 'Judge Middle Name',
 4 'Suffix',
 'Birth month',
 'Birth day',
 'Birth year',
 'Place of Birth (City)',
 'Place of Birth (State)',
 'Death month',
 'Death day',
 'Death year',
 'Place of Death (City)',
 'Place of Death (State)',
 'Gender',
 'Race or Ethnicity',
 17'Judge Identification Number',
 18 'Court Name',
 19 'Court Type',
 'President name',
 'Party Affiliation of President',
 'Renominating President name',
 'Party Affiliation of Renominating President',
 'Nomination Date Senate Executive Journal',
 'ABA Rating',
 'Recess Appointment date',
 'Vice last name (predecessor)',
 'Vice first name (predecessor)',
 'Authorization legislation',
 'Referral date (referral to Judicial Committee)',
 'Report number',
 'Committee action',
 'Committee action date',
 'Hearings',
 'Senate voice vote',
 'Senate vote Ayes/Nays',
 'Senate Vote Date (Confirmation Date)',
 'Commission Date',
 'Commission Year',
 'Date of Service as Chief Judge (begin)',
 'Date of Service as Chief Judge (end)',
 'Second Date of Service as Chief Judge (begin)',
 'Second Date of Service as Chief Judge (end)',
 'Retirement from Active Service',
 'Date of Termination',
 45'Termination specific reason',
 46'Judge Identification Number',
 47'Court Name (2)',
 48'Court Type (2)',
 'President name (2)',
 'Party Affiliation of President (2)',
 'Renominating President name (2)',
 'Party Affiliation of Renominating President (2)',
 'Nomination Date Senate Executive Journal (2)',
 'ABA Rating (2)',
 'Recess Appointment date (2)',
 'Vice last name (predecessor) (2)',
 'Vice first name (predecessor) (2)',
 'Authorization legislation (2)',
 'referral date (referral to Judicial Committee) (2)',
 'Report number (2)',
 'committee action (2)',
 'Committee action date (2)',
 'Hearings (2)',
 'Senate voice vote (2)',
 'Senate vote Ayes/Nays (2)',
 'Senate Vote Date (Confirmation Date) (2)',
 'Commission Date (2)',
 'Date of Service as Chief Judge (begin) (2)',
 'Date of Service as Chief Judge (end) (2)',
 'Second Date of Service as Chief Judge (begin) (2)',
 'Second Date of Service as Chief Judge (end) (2)',
 'Retirement from Active Service (2)',
 'Date of Termination (2)',
 74 'Termination specific reason (2)',
 75'Judge Identification Number',
 76'Court Name (3)',
 77'Court Type (3)',
 'President name (3)',
 'Party Affiliation of President (3)',
 'Renominating President name (3)',
 'Party Affiliation of Renominating President (3)',
 'Nomination Date Senate Executive Journal (3)',
 'ABA Rating (3)',
 'Recess Appointment date (3)',
 'Vice last name (predecessor) (3)',
 'Vice first name (predecessor) (3)',
 'Authorization legislation (3)',
 'referral date (referral to Judicial Committee) (3)',
 'Report number (3)',
 'committee action (3)',
 'Committee action date (3)',
 'Hearings (3)',
 'Senate voice vote (3)',
 'Senate vote Ayes/Nays (3)',
 'Senate Vote Date (Confirmation Date) (3)',
 'Commission Date (3)',
 'Date of Service as Chief Judge (begin) (3)',
 'Date of Service as Chief Judge (end) (3)',
 'Second Date of Service as Chief Judge (begin) (3)',
 'Second Date of Service as Chief Judge (end) (3)',
 'Retirement from Active Service (3)',
 'Date of Termination (3)',
 103'Termination specific reason (3)',
 104'Judge Identification Number',
 105'Court Name (4)',
 106'Court Type (4)',
 'President name (4)',
 'Party Affiliation of President (4)',
 'Renominating President name (4)',
 'Party Affiliation of Renominating President (4)',
 'Nomination Date Senate Executive Journal (4)',
 'ABA Rating (4)',
 'Recess Appointment date (4)',
 'Vice last name (predecessor) (4)',
 'Vice first name (predecessor) (4)',
 'Authorization legislation (4)',
 'referral date (referral to Judicial Committee) (4)',
 'Report number (4)',
 'committee action (4)',
 'Committee action date (4)',
 'Hearings (4)',
 'Senate voice vote (4)',
 'Senate vote Ayes/Nays (4)',
 'Senate Vote Date (Confirmation Date) (4)',
 'Commission Date (4)',
 'Date of Service as Chief Judge (begin) (4)',
 'Date of Service as Chief Judge (end) (4)',
 'Second Date of Service as Chief Judge (begin) (4)',
 'Second Date of Service as Chief Judge (end) (4)',
 'Retirement from Active Service (4)',
 'Date of Termination (4)',
 132'Termination specific reason (4)',
 133'Judge Identification Number',
 134'Court Name (5)',
 135'Court Type (5)',
 'President name (5)',
 'Party Affiliation of President (5)',
 'Renominating President name (5)',
 'Party Affiliation of Renominating President (5)',
 'Nomination Date Senate Executive Journal (5)',
 'ABA Rating (5)',
 'Recess Appointment date (5)',
 'Vice last name (predecessor) (5)',
 'Vice first name (predecessor) (5)',
 'Authorization legislation (5)',
 'referral date (referral to Judicial Committee) (5)',
 'Report number (5)',
 'committee action (5)',
 'Committee action date (5)',
 'Hearings (5)',
 'Senate voice vote (5)',
 'Senate vote Ayes/Nays (5)',
 'Senate Vote Date (Confirmation Date) (5)',
 'Commission Date (5)',
 'Date of Service as Chief Judge (begin) (5)',
 'Date of Service as Chief Judge (end) (5)',
 'Second Date of Service as Chief Judge (begin) (5)',
 'Second Date of Service as Chief Judge (end) (5)',
 'Retirement from Active Service (5)',
 'Date of Termination (5)',
 161'Termination specific reason (5)',
 162'Judge Identification Number',
 163'Court Name (6)',
 164'Court Type (6)',
 'President name (6)',
 'Party Affiliation of President (6)',
 'Nomination Date Senate Executive Journal (6)',
 'Renominating President name (6)',
 'Party Affiliation of Renominating President (6)',
 'ABA Rating (6)',
 'Recess Appointment date (6)',
 'Vice last name (predecessor) (6)',
 'Vice first name (predecessor) (6)',
 'Authorization legislation (6)',
 'referral date (referral to Judicial Committee) (6)',
 'Report number (6)',
 'committee action (6)',
 'Committee action date (6)',
 'Hearings (6)',
 'Senate voice vote (6)',
 'Senate vote Ayes/Nays (6)',
 'Senate Vote Date (Confirmation Date) (6)',
 'Commission Date (6)',
 'Date of Service as Chief Judge (begin) (6)',
 'Date of Service as Chief Judge (end) (6)',
 'Second Date of Service as Chief Judge (begin) (6)',
 'Second Date of Service as Chief Judge (end) (6)',
 'Retirement from Active Service (6)',
 'Date of Termination (6)',
 'Termination specific reason (6)',
 'Name of School',
 'Degree',
 'Degree year',
 'Name of School (2)',
 'Degree (2)',
 'Degree year (2)',
 'Name of School (3)',
 'Degree (3)',
 'Degree year (3)',
 'Name of School (4)',
 'Degree (4)',
 'Degree year (4)',
 'Name of School (5)',
 'Degree  (5)',
 'Degree year (5)',
 'Employment text field',
 'Bankruptcy and Magistrate service']


