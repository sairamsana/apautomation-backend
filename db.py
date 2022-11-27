from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine

# Server="SANA"
# Database="apautomation"
# Driver="ODBC Driver 17 for SQL Server"
# db_con = f'mssql://@{Server}/@{Database}?driver={Driver}'

# engine = create_engine(db_con)
# con = engine.connect()

db = SQLAlchemy()