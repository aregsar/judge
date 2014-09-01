
from flask_failsafe import failsafe
from flask.ext.script import Manager

#failsafe avoid server process from exiting if it encounters syntax errors
#when code is modified and saved
@failsafe
def create_app():
    from flask import Flask
    #from flask.ext.script import Manager
    from config import Config
    from routes import add_url_rules
    from views import home
    #from views import review


    #create the application context
    app = Flask(__name__)
    #manager = Manager(app)

    #configure application
    #config = Config()
    #app.config.from_object(config)
    app.config.from_object(Config)

    #optionally add url routing rules instead of route attributes
    #before registering blueprints
    add_url_rules()

    #register blueprints
    app.register_blueprint(home.mod)
    #app.register_blueprint(review.mod)


    @app.errorhandler(500)
    def internal_server_error(e):
        return "Judge internal server error"

    return app


#manage from commanc line
manager = Manager(create_app())

if __name__ == '__main__':
    manager.run()

