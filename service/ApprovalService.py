import uuid
from flask import request,jsonify,make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ApprovalsModel, BillModel
from schemas.schemas import ApprovalBillSchema
import pprint
from database.SQLSession import session,db_persist

blp = Blueprint("Approval", __name__, description="Operations on Approval")

@blp.route("/approval")
class ApprovalService(MethodView):

    @blp.arguments(ApprovalBillSchema)
    @db_persist
    @blp.response(201,ApprovalBillSchema)
    def post(self,approvalData):
        try:
            billid = approvalData['bills']['billid']
            res = session.query(BillModel).get(billid)
            if not res:
                abort(404,message="Approavl not found")
            print(res.as_dict())
            approval = ApprovalsModel(status=approvalData['status'],approved_by=approvalData['approved_by'],comments=approvalData['approved_by'])
            approval.billl = res
            # user.depts = depts
            session.merge(approval)
            session.flush()
            return res
        except KeyError:
            abort(404,message="user not found")

    @db_persist
    @blp.response(200,ApprovalBillSchema(many=True))
    def get(self):
        try:
            res = session.query(ApprovalsModel).all()
            return res
        except KeyError:
            abort(404,message="user not found")


@blp.route("/approval/<string:user_id>")
class ApprovalServiceById(MethodView):

    @blp.arguments(ApprovalBillSchema)
    @db_persist
    @blp.response(201,ApprovalBillSchema)
    def put(self,userData,user_id):
        try:
            res = session.query(ApprovalsModel).get(user_id)
            if not res:
                abort(404,message="user not found")
            user = ApprovalsModel(**userData)
            user.userid = res.userid
            session.merge(user)
            session.flush()
            return user
        except KeyError:
            abort(404,message="user not found")

    @db_persist
    @blp.response(200,ApprovalBillSchema)
    def get(self,user_id):
        try:
            res = session.query(ApprovalsModel).get(user_id)
            return res
        except KeyError:
            abort(404,message="user not found")
    
    @db_persist
    def delete(self,user_id):
        try:
            res = session.query(ApprovalsModel).get(user_id)
            if not res:
                abort(404,message="user not found")
            session.delete(res)
            return {"message":"deleted successfully"}
        except KeyError:
            abort(404,message="user not found")