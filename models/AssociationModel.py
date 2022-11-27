from sqlalchemy import Identity, Column, Integer, String, BINARY,Table,ForeignKey
from database.SQLSession import Base
import uuid
def generate_uuid():
    return str(uuid.uuid4())

association_table = Table(
    "user_dept",
    Base.metadata,
    Column('userdeptid', String, primary_key=True, default=generate_uuid),
    Column("userid", ForeignKey("user.userid"), primary_key=True),
    Column("deptid", ForeignKey("department.deptid"), primary_key=True),
)
