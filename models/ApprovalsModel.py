# from db import db
from sqlalchemy import Identity, Column, FLOAT, String, TEXT,DateTime,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
import uuid
from models.AssociationModel import association_table
from sqlalchemy.sql import func
# from models import UserDept
from database.SQLSession import Base

def generate_uuid():
    return str(uuid.uuid4())



class ApprovalsModel(Base):
    __tablename__ = 'approvals'
    approvalid = Column(String(256), primary_key=True, default=generate_uuid)
    status = Column(String(64), nullable=False)
    approved_by = Column(String(256), nullable=False)
    approved_on = Column(DateTime, nullable=False, default=func.now())
    comments = Column(String(256), nullable=False)
    billid = Column(String(256), ForeignKey("bills.billid"))
    billl = relationship("BillModel",back_populates="approvals")
    
    
    def __init__(self,status,approved_by,comments):
        self.status = status
        self.approved_by = approved_by
        self.comments = comments
