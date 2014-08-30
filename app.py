from flask import Flask
from flask.ext.script import Manager
from config import Config
#from views.home import home

#create the application context
app = Flask(__name__)
manager = Manager(app)

#configure application
config = Config()
app.config.from_object(config)
#app.config['DEBUG']=True




#register blueprints
#from blueprints import register_blueprints
#register_blueprints(app)
from views import home
home.mod.add_url_rule('/', endpoint='index',view_func=home.index)
app.register_blueprint(home.mod)
#app.register_blueprint(home)

#add url routing rules
#from routes import register_routes
#register_routes(app)
#app.add_url_rule('/api/<item_group>', defaults={'item_id': None},view_func=api_view, methods=['GET',])


#app.add_url_rule('/', endpoint='home.index')
#app.add_url_rule('/', endpoint='index')


#manage from commanc line
if __name__ == '__main__':
    manager.run()

