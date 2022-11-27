from marshmallow import Schema,fields

class DepartmentSchema(Schema):
    deptid = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class DepartmentUpdateSchema(Schema):
    deptid = fields.Str(required=True)
    name = fields.Str(required=False)

class UserSchema(Schema):
    userid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    mobile = fields.Str(required=True)
    status = fields.Boolean(required=True)
    usertype = fields.Str(required=True)
    password = fields.Str(required=True)

class UserBillSchema(Schema):
    userid = fields.Str(required=True)
    name = fields.Str(required=True)
    status = fields.Boolean(required=True)

class BillSchema(Schema):
    billid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    amount = fields.Float(required=True)
    tax = fields.Float(required=True)
    billdate = fields.Date(required=True)
    deptname = fields.Str(required=True)

class BillIDSchema(Schema):
    billid = fields.Str(required=True)
    name = fields.Str(required=True)


class ApprovalSchema(Schema):
    approvalid = fields.Str(dump_only=True)
    status = fields.Str(required=True)
    approved_by = fields.Str(required=True)
    comments = fields.Str(required=True)

class UserDeptSchema(UserSchema):
    depts = fields.List(fields.Nested(DepartmentUpdateSchema()))
    bills = fields.List(fields.Nested(BillSchema()))

class BillApprovalSchema(BillSchema):
    user = fields.Nested(UserBillSchema())
    approvals = fields.List(fields.Nested(ApprovalSchema()))

class ApprovalBillSchema(ApprovalSchema):
    bills = fields.Nested(BillIDSchema())