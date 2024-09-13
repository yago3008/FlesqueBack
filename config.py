class Config:
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://CA-C-00657\SQLEXPRESS/flesque?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///newflesquedb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'flesque'