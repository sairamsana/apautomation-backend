# from db import db
from sqlalchemy import Identity, Column, Integer, String,DateTime
from sqlalchemy.orm import declarative_base,relationship
import uuid
from models.AssociationModel import association_table
# from models import UserDept
from database.SQLSession import Base
import datetime

def generate_uuid():
    return str(uuid.uuid4())


class DepartmentModel(Base):
    __tablename__ = 'department'
    deptid = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String(256), unique=False, nullable=False)
    users = relationship("UserModel", secondary=association_table, back_populates="depts")

    def __init__(self,name,deptid=None):
        self.name = name
        if deptid:
            self.deptid = deptid
    
