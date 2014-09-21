
#utility module for recreating database in development
from app import create_app
app = create_app()
with app.app_context():
    from models.user import User, create_admin_users
    from models.judge import Judge,create_judges
    from models.judgereview import JudgeReview
    from plugins import db
    print db
    db.drop_all()
    db.create_all()
    user = User.query.filter_by(username="areg").first()
    print user
    if user == None:
        create_admin_users()
    user = User.query.filter_by(username="areg").first()
    #create_judges()
    print user

#work with the database
#$psql judgedb
#list tables in judgedb
#judgedb \d
#judgedb=# SELECT * FROM pg_catalog.pg_tables
