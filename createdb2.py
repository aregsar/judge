from app import create_app
app = create_app()
#app.run(debug=true)
with app.app_context():
    from models.user import User
    from plugins import db
    print db
    db.drop_all()
    db.create_all()
    user = User.query.filter_by(email="test").first()
    print user

#work with the database
#$psql judgedb
#list tables in judgedb
#judgedb \d
#judgedb=# SELECT * FROM pg_catalog.pg_tables
