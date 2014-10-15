from app import create_app
app = create_app()
with app.app_context():
    from models.judgedata import JudgeDataRecord,JudgeData
    JudgeDataRecord.load_file_data('migrations/judges.csv')
