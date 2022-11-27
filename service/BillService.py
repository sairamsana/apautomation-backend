import uuid
from flask import request,jsonify,make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import BillModel, UserModel
from schemas.schemas import BillApprovalSchema,UserDeptSchema
import pprint
from database.SQLSession import session,db_persist

blp = Blueprint("Bills", __name__, description="Operations on bill profile")

@blp.route("/bill")
class BillService(MethodView):

    @blp.arguments(BillApprovalSchema)
    @db_persist
    @blp.response(201,BillApprovalSchema)
    def post(self,billData):
        try:
            bill =  BillModel(name=billData['name'],amount=billData['amount'],tax=billData['tax'],billdate=billData['billdate'],deptname=billData['deptname'])
            pprint.pprint(billData)
            pprint.pprint(billData['user']['userid'])
            userid = billData['user']['userid']
            user = session.query(UserModel).get(userid)
            bill.user = user
            pprint.pprint(user)
            session.merge(bill)
            session.flush()
            return bill
        except KeyError:
            abort(404,message="user not found")

    @db_persist
    @blp.response(200,BillApprovalSchema(many=True))
    def get(self):
        try:
            res = session.query(BillModel).all()
            return res
        except KeyError:
            abort(404,message="user not found")


@blp.route("/bill/<string:user_id>")
class BillServiceById(MethodView):

    @blp.arguments(UserDeptSchema)
    @db_persist
    @blp.response(201,UserDeptSchema)
    def put(self,userData,user_id):
        try:
            res = session.query(UserModel).get(user_id)
            if not res:
                abort(404,message="user not found")
            user = UserModel(**userData)
            user.userid = res.userid
            session.merge(user)
            session.flush()
            return user
        except KeyError:
            abort(404,message="user not found")

    @db_persist
    @blp.response(200,BillApprovalSchema)
    def get(self,user_id):
        try:
            res = session.query(BillModel).get(user_id)
            return res
        except KeyError:
            abort(404,message="user not found")
    
    @db_persist
    def delete(self,user_id):
        try:
            res = session.query(UserModel).get(user_id)
            if not res:
                abort(404,message="user not found")
            session.delete(res)
            return {"message":"deleted successfully"}
        except KeyError:
            abort(404,message="user not found")