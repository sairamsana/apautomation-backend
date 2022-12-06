import json
import uuid
import os
from flask import request, jsonify, make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ApprovalsModel, BillModel, UserModel
from schemas.schemas import BillAndApprovalSchema, BillApprovalSchema, BillSchema, BillUploadSchema, UserDeptSchema
import pprint
from database.SQLSession import sqlsession, db_persist
from werkzeug.utils import secure_filename
from Commons.Constants import Constants
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.sql import label
from flask import Response

blp = Blueprint("Bills", __name__, description="Operations on bill profile")


@blp.route("/bills")
class BillService(MethodView):

    # @blp.arguments(BillApprovalSchema)
    # @db_persist
    # @blp.response(201,BillApprovalSchema)
    # def post(self,billData):
    #     try:
    #         bill =  BillModel(name=billData['name'],amount=billData['amount'],tax=billData['tax'],billdate=billData['billdate'],deptname=billData['deptname'])
    #         pprint.pprint(billData)
    #         pprint.pprint(billData['user']['userid'])
    #         userid = billData['user']['userid']
    #         user = sqlsession.query(UserModel).get(userid)
    #         bill.user = user
    #         pprint.pprint(user)
    #         sqlsession.merge(bill)
    #         sqlsession.flush()
    #         return bill
    #     except KeyError:
    #         abort(404,message="user not found")

    @db_persist
    def post(self):
        data = request.form.to_dict()
        pprint.pprint(data)
        try:
            target = os.path.join(Constants.UPLOAD_FOLDER)
            if not os.path.isdir(target):
                os.mkdir(target)
            file = request.files['setImage']
            filename = secure_filename(file.filename)
            destination = "/".join([target,filename])
            bill =  BillModel(name=request.form['name'],amount=request.form['amount'],tax=request.form['tax'],billdate=request.form['billdate'],deptname=request.form['deptname'],filename=filename,retail=request.form['retail'],billstatus=request.form['billstatus'])
            userid = request.form['userid']
            user = sqlsession.query(UserModel).get(userid)
            bill.user = user
            userobj = user.as_dict()
            print(userobj['name'])
            file.save(destination)

            approval = ApprovalsModel(
                status='Pending', approved_by=userobj['name'], comments='')
            approval.billl = bill
            sqlsession.merge(bill)

            sqlsession.flush()
            return {'status':'success', 'message':'bill submitted successfully'},201
        except KeyError:
            abort(404, message="Bll not found")

    @db_persist
    @blp.response(200, BillApprovalSchema(many=True))
    def get(self):
        try:
            res = sqlsession.query(BillModel).order_by(BillModel.billdate).all()
            return res
        except KeyError:
            abort(404, message="user not found")


@blp.route("/bills/<string:user_id>")
class BillServiceByUserId(MethodView):

    @blp.arguments(UserDeptSchema)
    @db_persist
    @blp.response(201, UserDeptSchema)
    def put(self, userData, user_id):
        try:
            res = sqlsession.query(UserModel).filter(UserModel.userid == user_id)
            if not res:
                abort(404, message="user not found")
            user = UserModel(**userData)
            user.userid = res.userid
            sqlsession.merge(user)
            sqlsession.flush()
            return user
        except KeyError:
            abort(404, message="user not found")

    @db_persist
    @blp.response(200, BillAndApprovalSchema(many=True))
    def get(self, user_id):
        try:
            print(user_id)
            res = sqlsession.query(BillModel).filter(BillModel.userid == user_id)
            return res
        except KeyError:
            abort(404, message="user not found")

    # @db_persist
    # def delete(self, user_id):
    #     try:
    #         res = sqlsession.query(UserModel).get(user_id)
    #         if not res:
    #             abort(404, message="user not found")
    #         sqlsession.delete(res)
    #         return {"message": "deleted successfully"}
    #     except KeyError:
    #         abort(404, message="user not found")


@blp.route("/bill/<string:billid>")
class BillServiceById(MethodView):

    @db_persist
    @blp.response(200, BillAndApprovalSchema)
    def get(self, billid):
        try:
            print(billid)
            res = sqlsession.query(BillModel).order_by("approvals.approved_on desc").get(billid)
            return res
        except KeyError:
            abort(404, message="user not found")


@blp.route("/billcount")
class BillApprovalsCount(MethodView):

    @db_persist
    # @blp.response(200, BillAndApprovalSchema)
    def get(self):
        try:
            # res = sqlsession.query(BillModel).order_by("approvals.approved_on desc").get(billid)
            res = sqlsession.query(BillModel.billstatus,label('Status', func.count(BillModel.billid))).group_by(BillModel.billstatus).all()
            print(list(res))
            results = {row[0]:row[1] for row in res}
            return Response(json.dumps(results),  mimetype='application/json')
        except KeyError:
            abort(404, message="user not found")