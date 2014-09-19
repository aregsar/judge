from app import create_app
app = create_app()
with app.app_context():
    from models.user import User
    from models.judge import Judge, CreateRetiredJudge
    from models.judgereview import JudgeReview
    from plugins import db
    print db
    db.drop_all()
    db.create_all()
    user = User.query.filter_by(username="areg").first()
    print user
    #judge = CreateRetiredJudge(name="areg")
    #judgereview = JudgeReview(judge_id=1,title="test review",body="bad judge",rating="1",username="areg",user_id=1)

#work with the database
#$psql judgedb
#list tables in judgedb
#judgedb \d
#judgedb=# SELECT * FROM pg_catalog.pg_tables
