from views import home
from views import account


def register_blueprints(app):
   app.register_blueprint(home.mod)
   app.register_blueprint(account.mod)
