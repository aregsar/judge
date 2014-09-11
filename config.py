import os

"""
single configuration class for all environments
defines all keys that will exist in all environments
(some keys may not be being used in some environments but that is OK)
The values for all keys are loaded from environment variables defined
in each environment. If the env var is not defined the key value will default
to None. A separate bash script that is not checked in to public
source control repo, should be created for each environment
which will set the environmet vars for that specific environment
"""
class Config:
    #ENV can be set to "DEV" or "TEST" or "STAGE" or "PROD"
    ENV = os.environ.get('FLASK_ENVIRONMET')
    DEBUG = bool(os.environ.get('FLASK_DEBUG'))
    SECRET_KEY = "test"
    #export DATABASE_URI=sqlite:///judgedoc
    #export DATABASE_URI=postgres://un:pwd@localhost/judgedb
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

    #python script for generating secret key from command line
    #python xxxxxx
    #SECRET_KEY = os.environ.get('FLASK_DEBUG')


    #In bash set rails to production
    #export RAILS_ENV=production
    #In rails migrator app add a production environment configuration
    #to the database.yml file
    #when rails starts up it loads all environment vars into an ENV hash
    #including the RAILS_ENV env var which can be accessed using ENV['RAILS_ENV']
    #via Rails.application.initialize! in the environment.rb file
    #we can set a default value if the env var is not created in the shell
    #in environment.rb file
    #ENV['RAILS_ENV'] ||= 'production'

    #heroku database management
    #$ heroku config | grep DATABASE_URL  --app herokuappname
    #$ heroku config | grep DATABASE_URL  --app judgejungle
    #DATABASE_URL => postgres://judgedb:ec2.amazonaws.com/judgedb
    #on the migrator heroku database management application (judgedb)
    #$ heroku config:add DATABASE_URL=postgres://judgedb:ec2.amazonaws.com/judgedb --app judgedatabase
    #$ heroku pg:promote DATABASE_URL --app judgejungle
    #$ heroku pg:promote DATABASE_URL --app judgejungledb

"""
Alteratively load a configuration file path for each environment
based on a path set by an env var
and load configuration from that file using
app.config.load_frompyfile(ConfigFile.CONFIG_FILE_PATH)
class ConfigFile:
    CONFIG_FILE_PATH = os.environ.get('FLASK_CONFIG_FILE_PATH')
"""
