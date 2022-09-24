''' Flask necessary imports '''
from datetime import datetime, timedelta
import os

''' Database filename config  '''
extension = ".db"
filename = "database"
database_file = filename + extension

''' Flask necessary imports '''
from flask import Flask, render_template,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

''' SQLALCHEMY configs '''
app = Flask(__name__, template_folder='../src')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
CORS(app)
db = SQLAlchemy(app)

''' JWT necessary imports '''
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

''' JWT configs '''
app.config["JWT_SECRET_KEY"] = "4f2db2f556daa6e107657ce3efbb0b5d-SUPER-SECRET"  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=5) 
jwt = JWTManager(app)