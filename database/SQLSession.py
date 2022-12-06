import pprint
from sqlalchemy.orm import sessionmaker,declarative_base
from database.DBConnector import Connector
from sqlalchemy import exc

engine = Connector()
Session = sessionmaker(bind=engine.get_connector())
sqlsession = Session()
Base = declarative_base()
def as_dict(self):
    return {item.name: getattr(self, item.name) for item in self.__table__.columns}

Base.as_dict = as_dict    


def db_persist(func):
    def persist(*args, **kwargs):
        res = func(*args, **kwargs)
        try:
            sqlsession.commit()
            return res
        except exc.SQLAlchemyError as e:
            sqlsession.rollback()
            return res
        finally:
            sqlsession.close()
            
    return persist