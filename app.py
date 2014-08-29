from flask import Flask
from views.home import home
from flask.ext.script import Manager
from config import Config

app = Flask(__name__)
manager = Manager(app)

#configure application
config = Config()
app.config.from_object(config)

#register blueprints
app.register_blueprint(home)

#run the server
if __name__ == '__main__':
    manager.run()

