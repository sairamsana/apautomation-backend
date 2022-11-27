# from db import db
from sqlalchemy import Identity, Column, Boolean, String, BINARY,Table,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
import uuid
from models.AssociationModel import association_table

# from models import UserDept
from database.SQLSession import Base

def generate_uuid():
    return str(uuid.uuid4())



class UserModel(Base):
    __tablename__ = 'user'
    userid = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String(256), unique=False, nullable=False)
    email = Column(String(128), unique=False, nullable=False)
    mobile = Column(String(15), unique=False, nullable=False)
    status = Column(Boolean, unique=False, nullable=False)
    usertype = Column(String(50), unique=False, nullable=False)
    password = Column(String(128), unique=False, nullable=False)
    depts = relationship("DepartmentModel", secondary=association_table, back_populates="users")
    bills = relationship("BillModel",back_populates="user")

    def __init__(self,name,email,mobile,status,usertype,password):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.status = status
        self.usertype = usertype
        self.password = password
