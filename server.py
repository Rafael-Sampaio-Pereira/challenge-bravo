from flask import Flask, request, make_response, jsonify
from flask_login import LoginManager, current_user
import sqlite3
from flask_cors import CORS
import os
from project.settings import HOST, PORT, DEBUG
from routes.auth import authRoutes
from routes.test import testRoutes
from routes.currency import currencyRoutes
from database.sharedConnector import db


api = Flask(__name__)
api.secret_key =  os.getenv('SECRET_KEY')
api.flask_run_port = PORT
api.flask_run_HOST = HOST
api.debug = DEBUG
api.threaded = True
CORS(api)
authManager = LoginManager(api)
authRoutes(api, authManager)
currencyRoutes(api)
testRoutes(api)

api.config ['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///database/{os.getenv('DB_NAME')}"
db.init_app(api)


api.run(HOST, PORT, threaded = True)

#docker run -p 8080:80 -it -e APP_MODULE="server:api" myimage