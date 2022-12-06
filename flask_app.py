# from crypt import methods
import json
from flask import Flask, request, session, Response
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
import urllib.request
from flask_cors import CORS
from Commons import Constants
from datetime import timedelta
from flask import send_from_directory
# from db import db


from service import DeptBluePrint, UserBluePrint, BillBluePrint, ApprovalBluePrint

app = Flask(__name__)

# login_check = auth.login_check
# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, automatic_options=True )

# CORS(app, supports_credentials=True, automatic_options=True)
# cors = [r"^https://(.).goupshot.com$", r"^https://(.).in.goupshot.com$"]
# CORS(app, supports_credentials=True, origins=cors)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = Constants.UPLOAD_FOLDER
# App Session Configuration
# app.permanent_session_lifetime = timedelta(days=30)
# app.secret_key = Constants.FLASK_SECRET
# app.config['SESSION_COOKIE_NAME'] = Constants.SESSION_COOKIE_NAME
# app.config['SESSION_COOKIE_DOMAIN'] = Constants.SESSION_DOMAIN
# app.config['SESSION_COOKIE_PATH'] = Constants.SESSION_COOKIE_PATH
# app.config['SESSION_COOKIE_SECURE'] = Constants.SESSION_SECURE
# app.config['SESSION_REFRESH_EACH_REQUEST'] = False
app.config['CORS_HEADERS'] = 'Content-Type'


app.config["API_TITLE"] = "APAutomation"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=SANA;DATABASE=apautomation;Trusted_Connection=yes;')
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
# db.init_app(app)


api = Api(app)

api.register_blueprint(DeptBluePrint)
api.register_blueprint(UserBluePrint)
api.register_blueprint(BillBluePrint)
api.register_blueprint(ApprovalBluePrint)


@app.route('/saved/bills/<path:path>')
def send_report(path):
    return send_from_directory(Constants.UPLOAD_FOLDER, path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5004', debug=True)
