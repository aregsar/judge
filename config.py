import os

class Config:
    DEBUG = bool(os.environ.get('FLASK_DEBUG'))
