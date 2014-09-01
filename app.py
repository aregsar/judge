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
#config = Config()
#app.config.from_object(config)
app.config.from_object(Config)
#app.config['DEBUG']=True

#install application wide global error hanlders
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

@app.before_first_request
def app_before_first_request():
    pass

@app.before_request
def app_before_request():
    pass

@app.after_request
def app_after_req(response):
    return response

@app.teardown_request
def app_teardown_request(response):
    return response

#optionally add url routing rules instead of route attributes (before registering blueprints)
add_url_rules()

#register blueprints
app.register_blueprint(home.mod)
#app.register_blueprint(review.mod)

#list all mapped routes
#app.url_map
#home.mod.url_map

#manage from commanc line
if __name__ == '__main__':
    manager.run()

