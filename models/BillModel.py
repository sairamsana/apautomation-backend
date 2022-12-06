# from db import db
from sqlalchemy import Identity, Column, FLOAT, String, BINARY,Date,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
import uuid
from models.AssociationModel import association_table

# from models import UserDept
from database.SQLSession import Base

def generate_uuid():
    return str(uuid.uuid4())



class BillModel(Base):
    __tablename__ = 'bills'
    billid = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String(256), unique=False, nullable=False)
    filename = Column(String(256), unique=False, nullable=False)
    billstatus = Column(String(256), unique=False, nullable=False)
    retail = Column(String(256), unique=False, nullable=False)
    amount = Column(FLOAT(128), unique=False, nullable=False)
    tax = Column(FLOAT(15), unique=False, nullable=False)
    billdate = Column(Date, unique=False, nullable=False)
    deptname = Column(String(50), unique=False, nullable=False)
    userid = Column(String(256), ForeignKey("user.userid"))
    user = relationship("UserModel", back_populates="bills")
    approvals = relationship("ApprovalsModel",back_populates="billl")

    def __init__(self,name,amount,tax,billdate,deptname,filename,retail,billstatus):
        self.name = name
        self.amount = amount
        self.tax = tax
        self.billdate = billdate
        self.deptname = deptname
        self.filename = filename
        self.retail = retail
        self.billstatus = billstatus