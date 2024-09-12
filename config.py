class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://DESKTOP-MVK7GJG\SQLEXPRESS/flesque?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'flesque'