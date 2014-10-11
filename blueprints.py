from views import home
from views import account
from views import judge
from views import review
from views import user
from views import company

#for each view blueprint you need to add corresponding blueprint registration here
def register_blueprints(app):
    app.register_blueprint(home.res)
    app.register_blueprint(account.mod)
    app.register_blueprint(judge.mod)
    app.register_blueprint(review.mod)
    app.register_blueprint(user.mod)
    app.register_blueprint(company.mod)
