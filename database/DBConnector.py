from sqlalchemy import create_engine
from database.Singleton import Singleton
from sqlalchemy.orm import sessionmaker
import urllib

@Singleton
class Connector:
    def __init__(self):
        self.connector = dict()

    def get_connector(self):
        params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=SANA;DATABASE=apautomation;Trusted_Connection=yes;')
        
        Server="SANA"
        Database="apautomation"
        Driver="ODBC Driver 17 for SQL Server"
        db_con = "mssql+pyodbc:///?odbc_connect=%s" % params
        engine = create_engine(db_con)
        # con = engine.connect()
        return engine