class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:flask@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'flesque'