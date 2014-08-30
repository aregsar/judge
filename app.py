from flask import Flask
from flask.ext.script import Manager
from config import Config
from routes import add_url_rules
from views import home
#from views import review


#create the application context
app = Flask(__name__)
manager = Manager(app)

#configure application
config = Config()
app.config.from_object(config)
#app.config['DEBUG']=True


#optionally add url routing rules instead of route attributes (before registering blueprints)
add_url_rules()

#register blueprints
app.register_blueprint(home.mod)
#app.register_blueprint(review.mod)


#manage from commanc line
if __name__ == '__main__':
    manager.run()

