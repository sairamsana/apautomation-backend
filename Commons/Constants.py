class Constants:
    FAIL = 'fail'
    SUCCESS = 'success'
    
    DATAINCONSISTANT = 'datainconsistant'

    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NOCONTENT = 204
    BADREQUEST = 400
    UNAUTHORIZED = 401
    PAYMENTREQUIRED = 402
    FORBIDDEN = 403
    NOTFOUND = 404
    METHODNOTALLOWED = 405
    REQUESTTIMEOUT = 408
    INTERNALSERVERERROR = 500
    NOTIMPLEMENTED = 501
    BADGATEWAY = 502
    SERVICEUNAVAILABLE = 503
    
    BASE_CLUSTER = 'c1'
    MAIN_REGION_BASE_URL = 'http://127.0.0.1:5004'

    SESSION_SECURE = False
    SESSION_DOMAIN = None
    SESSION_COOKIE_NAME = "jkfomo"
    SESSION_COOKIE_PATH = ""
    TOKEN_SESSION_TIME_MINS = 30
    SESSION_TIME_DAYS = 31
    FLASK_SECRET = 'svnpjpjrhhqtsqbxroko'

    # dont change salk key at any reason
    SALK_KEY = '88cb71c9c7e0b8cc065ef32639ac166f'

    # sairamsana88cb71c9c7e0b8cc065ef32639ac166f

    # DB Connection
    DB_URL = 'localhost'
    DB_PORT = 27017
    DB_Auth = False
    DB_USERNAME = ''
    DB_PASSWORD = ''