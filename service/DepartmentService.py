import uuid
from flask import request,jsonify,make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import DepartmentModel
from schemas.schemas import DepartmentSchema
import pprint
from database.SQLSession import sqlsession,db_persist

blp = Blueprint("Department", __name__, description="Operations on department")

@blp.route("/department")
class DepartmentService(MethodView):

    @blp.arguments(DepartmentSchema)
    @db_persist
    @blp.response(201,DepartmentSchema)
    def post(self,deptData):
        pprint.pprint(deptData)
        try:
            dept = DepartmentModel(**deptData)
            sqlsession.add(dept)
            sqlsession.flush()
            return dept
        except KeyError:
            abort(404,message="dept not found")

    @db_persist
    @blp.response(200,DepartmentSchema(many=True))
    def get(self):
        try:
            res = sqlsession.query(DepartmentModel).all()
            return res
        except KeyError:
            abort(404,message="user not found")


@blp.route("/department/<string:dept_id>")
class DepartmentServiceById(MethodView):

    @blp.arguments(DepartmentSchema)
    @db_persist
    @blp.response(201,DepartmentSchema)
    def put(self,deptData,dept_id):
        try:
            res = sqlsession.query(DepartmentModel).get(dept_id)
            if not res:
                abort(404,message="dept not found")
            dept = DepartmentModel(**deptData)
            dept.deptid = res.deptid
            sqlsession.merge(dept)
            sqlsession.flush()
            return dept
        except KeyError:
            abort(404,message="dept not found")

    @db_persist
    @blp.response(200,DepartmentSchema)
    def get(self,dept_id):
        try:
            res = sqlsession.query(DepartmentModel).get(dept_id)
            return res
        except KeyError:
            abort(404,message="user not found")
    
    @db_persist
    def delete(self,dept_id):
        try:
            res = sqlsession.query(DepartmentModel).get(dept_id)
            if not res:
                abort(404,message="dept not found")
            sqlsession.delete(res)
            return {"message":"deleted successfully"}
        except KeyError:
            abort(404,message="user not found")