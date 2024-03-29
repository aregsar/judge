from flask import Flask, g
from config import Config
from routes import add_url_rules
from blueprints import register_blueprints
from functools import wraps
from plugins import init_plugins
#from flask_failsafe import failsafe
#from models.user import User

#@failsafe
def create_app():
    #
    #create the root application context
    app = Flask(__name__)

    #
    #configure application(before initializing plugins)
    app.config.from_object(Config)

    #
    #setup flask extensions
    init_plugins(app)

    #
    #add any aditional url routing rules (before registering blueprints)
    add_url_rules()

    #
    #register blueprints
    register_blueprints(app)

    #
    #install application wide error handlers
    @app.errorhandler(404)
    def not_found(e):
        return "not found"
        #return app.send_static_file("html/errors/404.html")


    @app.errorhandler(500)
    def internal_server_error(e):
        return "internal server error"
        #return app.send_static_file("html/errors/500.html")

    #
    #install application wide request filters
    @app.before_first_request
    def app_before_first_request():
        pass

    @app.before_request
    def app_before_request():
        #g.db = connect_db()
        g.current_user = 1
        print g.current_user

    @app.after_request
    def app_after_req(response):
        curr_user = getattr(g, 'current_user', None)
        if curr_user is not None:
            g.current_user = 2
            print g.current_user
        return response

    @app.teardown_request
    def app_teardown_request(exception):
        db = getattr(g, 'db', None)
        if db is not None:
            #db.close()
            print g.db
        curr_user = getattr(g, 'current_user', None)
        if curr_user is not None:
            g.current_user = 3
            print g.current_user


    #
    #list all application mapped routes
    print app.url_map

    return app

#
#manage from command line
from flask.ext.script import Manager
judgeapp = create_app()
manager = Manager(judgeapp)
if __name__ == '__main__':
    manager.run()

