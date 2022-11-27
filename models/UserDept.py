# from sqlalchemy import Identity, Column, Integer, String,ForeignKey
# from sqlalchemy.orm import declarative_base,relationship
# import uuid
# from database.SQLSession import Base


# class UserDept(Base):
#     __tablename__ = "user_dept"
#     userdeptid = Column(String, primary_key=True)
#     deptid = Column(String, ForeignKey('dept.deptid'))
#     userid = Column(String, ForeignKey('user.userid'))