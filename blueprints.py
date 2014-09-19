from views import home
from views import account
from views import judge

def register_blueprints(app):
   app.register_blueprint(home.mod)
   app.register_blueprint(account.mod)
   app.register_blueprint(judge.mod)
