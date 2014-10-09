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
    #use $ env or $ printenv to show current env var settings

    #ENV can be set to "DEV" or "TEST" or "STAGE" or "PROD"
    ENV = os.environ.get('FLASK_ENVIRONMENT')
    DEBUG = bool(os.environ.get('FLASK_DEBUG'))
    #SSL_DISABLE = False

    #SqlAlchemy looks for this specific app.config['SQLALCHEMY_DATABASE_URL']
    #export DATABASE_URL='postgres://localhost/judgedb'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True

    #secret key generation from python shell
    #import os
    #os.urandom(24)
    #export SECRET_KEY='\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD'
    SECRET_KEY = os.environ['SECRET_KEY']
    #SECRET_KEY = os.environ.get('JUDGE_SECRET_KEY')

    JUDGE_JUDGES_PER_PAGE = 20
    JUDGE_JUDGE_REVIEWS_PAGE = 50
    JUDGE_USERS_PER_PAGE = 30
    JUDGE_SLOW_DB_QUERY_TIME=0.5



        ## Fixup the reverse proxy server headers
        ## when SSL termination happens at load balancer proxy
        # from werkzeug.contrib.fixers import ProxyFix
        # app.wsgi_app = ProxyFix(app.wsgi_app)

        ## Heroku Logging
        ## log to stderr
        # @classmethod
        # def init_app(cls, app):
        #   import logging
        #   from logging import StreamHandler
        #   file_handler = StreamHandler()
        #   file_handler.setLevel(logging.WARNING)
        #   app.logger.addHandler(file_handler)

        ## SysLog Logging
        ## log to syslog
        # @classmethod
        # def init_app(cls, app):
        #   import logging
        #   from logging.handlers import SysLogHandler
        #   syslog_handler = SysLogHandler()
        #   syslog_handler.setLevel(logging.WARNING)
        #   app.logger.addHandler(syslog_handler)


    #app has these special config keys as properties???
    #app.secret_key
    #app.config['SECRET_KEY']
    #app.debug
    #app.config['DEBUG']

    #SECRET_KEY = "test"
    #export DATABASE_URI=sqlite:///judgedoc
    #export DATABASE_URI=postgres://un:pwd@localhost/judgedb
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
