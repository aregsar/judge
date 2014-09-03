from flask import Flask, g
from config import Config
from routes import add_url_rules
from views import home
#from views import review

#
#create the root application context
app = Flask(__name__)

#
#configure application
app.config.from_object(Config)

#
#install application wide error hanlders
@app.errorhandler(404)
def not_found(e):
    return "Judge not found"
    #return render_template("static/404.html"), 404
    #return render_template("static/html/404.html"), 404
    #return render_template("templates/404.html"), 404
    #return render_template("templates/errors/404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return "Judge internal server error"
    #return render_template("static/html/404.html"), 404

#
#install application wide request filters
@app.before_first_request
def app_before_first_request():
    #initialize database
    pass

@app.before_request
def app_before_request():
    g.db = 10
    g.current_user = 1
    print g.current_user

@app.after_request
def app_after_req(response):
    if g.current_user:
        g.current_user = 2
        print g.current_user
    return response

@app.teardown_request
def app_teardown_request(exception):
    if g.db:
        g.db#.close()
    if g.current_user:
        g.current_user = 3
        print g.current_user

#
#add any aditional url routing rules (before registering blueprints)
add_url_rules()

#
#register blueprints
#register_blueprints(app)
app.register_blueprint(home.mod)
#app.register_blueprint(review.mod)

#
#list all mapped routes
#app.url_map
#home.mod.url_map


#
#manage from command line
from flask.ext.script import Manager
manager = Manager(app)
if __name__ == '__main__':
    manager.run()

