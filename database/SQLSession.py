import pprint
from sqlalchemy.orm import sessionmaker,declarative_base
from database.DBConnector import Connector
from sqlalchemy import exc

engine = Connector()
Session = sessionmaker(bind=engine.get_connector())
session = Session()
Base = declarative_base()
def as_dict(self):
    return {item.name: getattr(self, item.name) for item in self.__table__.columns}

Base.as_dict = as_dict    


def db_persist(func):
    def persist(*args, **kwargs):
        res = func(*args, **kwargs)
        try:
            session.commit()
            return res
        except exc.SQLAlchemyError as e:
            session.rollback()
            return res
        finally:
            session.close()
            
    return persist