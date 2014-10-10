
#utility module for recreating database in development
from app import create_app
app = create_app()
with app.app_context():
    from models.user import User, create_test_users
    from models.judge import Judge,create_test_judges
    from models.judgereview import JudgeReview
    from models.userjudge import UserJudge
    from models.candidate import Candidate
    from plugins import db
    print db
    db.drop_all()
    db.create_all()
    user = User.query.filter_by(username="areg").first()
    print user
    if user == None:
        create_test_users()
    user = User.query.filter_by(username="areg").first()
    print user
    judge = Judge.query.filter_by(name="areg").first()
    if judge == None:
        create_test_judges()
    judge = Judge.query.filter_by(name="areg").first()
    print judge

#can_view_resource(current_user,resource_owner_user,resource=None)
#can_edit_resource(current_user,resource_owner_user,resource=None)
#can_approve_resource(current_user,resource_owner_user,resource=None)
#can_destroy_resource(current_user,resource_owner_user,resource=None)

#work with the database
#$psql judgedb
#list all databases
#judgedb \l
#list tables in judgedb
#judgedb \d
#judgedb=# SELECT * FROM pg_catalog.pg_tables
