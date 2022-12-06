import uuid
from flask import request, jsonify, make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from Commons import Constants
from models import DepartmentModel, UserModel
from schemas.schemas import UserLogin, UserSchema, UserDeptSchema
import pprint
from sqlalchemy import select
from database.SQLSession import sqlsession, db_persist
from flask import jsonify, session

blp = Blueprint("User", __name__, description="Operations on user profile")


@blp.route("/user")
class UserService(MethodView):

    @blp.arguments(UserDeptSchema)
    @db_persist
    @blp.response(201, UserDeptSchema)
    def post(self, userData):
        try:
            depts = []
            for d in userData['depts']:
                depts.append(DepartmentModel(
                    name=d['name'], deptid=d['deptid']))
            user = UserModel(name=userData['name'], email=userData['email'], mobile=userData['mobile'],
                             status=userData['status'], usertype=userData['usertype'], password=userData['password'])
            user.depts = depts
            sqlsession.merge(user)
            sqlsession.flush()
            return user
        except KeyError:
            abort(404, message="user not found")

    @db_persist
    @blp.response(200, UserDeptSchema(many=True))
    def get(self):
        try:
            res = sqlsession.query(UserModel).all()
            # res = [obj.as_dict() for obj in res]
            return res
        except KeyError:
            abort(404, message="user not found")


@blp.route("/user/<string:user_id>")
class UserServiceById(MethodView):

    @blp.arguments(UserDeptSchema)
    @db_persist
    @blp.response(201, UserDeptSchema)
    def put(self, userData, user_id):
        try:
            res = sqlsession.query(UserModel).get(user_id)
            if not res:
                abort(404, message="user not found")
            depts = []
            for d in userData['depts']:
                depts.append(DepartmentModel(
                    name=d['name'], deptid=d['deptid']))
            user = UserModel(name=userData['name'], email=userData['email'], mobile=userData['mobile'],
                             status=userData['status'], usertype=userData['usertype'], password=userData['password'])
            user.depts = depts
            user.userid = res.userid
            print(user.userid)
            sqlsession.merge(user)
            sqlsession.flush()
            return user
        except KeyError:
            abort(404, message="user not found")

    @db_persist
    @blp.response(200, UserDeptSchema)
    def get(self, user_id):
        try:
            res = sqlsession.query(UserModel).get(user_id)
            return res
        except KeyError:
            abort(404, message="user not found")

    @db_persist
    def delete(self, user_id):
        try:
            res = sqlsession.query(UserModel).get(user_id)
            if not res:
                abort(404, message="user not found")
            print(res.as_dict())
            status = (res.as_dict()['status'])
            print(status)
            # sqlsession.delete(res)
            return {"message": "deleted successfully"}
        except KeyError:
            abort(404, message="user not found")


@blp.route("/login")
class UserService(MethodView):

    @blp.arguments(UserLogin)
    @db_persist
    def post(self, userData):
        try:
            res = sqlsession.query(UserModel).filter(
                UserModel.email == userData['email'], UserModel.password == userData['password']).first()
            if res == None:
                return {'status': Constants.FAIL, 'message': 'Username or password invalid'}, 404
            if res.email == userData['email'] and res.password == userData['password']:
                # session["username"] = str(res.userid)
                return {'userid': str(res.userid), 'name': res.name, 'email': res.email,'usertype': res.usertype, 'status': True}, 200
        except KeyError:
            abort(404, message="user not found")
