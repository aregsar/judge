judge
=====

[
    {"keys": ["f5"], "command": "refresh_folder_list" }
]


(venv)$ pip install -r requirements.txt
(venv)$ pip freeze > requirements.txt


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

