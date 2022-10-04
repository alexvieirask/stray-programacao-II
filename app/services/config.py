''' Extra imports '''
from datetime import datetime, timedelta
import os


''' Database filename config  '''
extension = ".db"
filename = "database"
database_file = filename + extension

''' typing config '''
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import flask_sqlalchemy
    import sqlalchemy.orm
    class Model(flask_sqlalchemy.Model):
        query: flask_sqlalchemy.BaseQuery
    
    class SQLAlchemy():
        Query = flask_sqlalchemy.BaseQuery
        Model = Model
        session = sqlalchemy.orm.scoped_session
    db: SQLAlchemy

''' Flask SQLALCHEMY imports '''
from flask import Flask, render_template,jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

''' Flask SQLALCHEMY configs '''
app = Flask(__name__, template_folder='../src', static_folder='../src/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

CORS(app)
db = SQLAlchemy(app)
db.session.execute('pragma foreign_keys=on')

''' JWT imports '''
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

''' JWT configs '''
app.config["JWT_SECRET_KEY"] = "faf1644b1743243a99f051f223464a66bdd665c2389b519f0d1d2a90c32efb6b-SUPER-SECRET-SUPER-SECRET"  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10) 
jwt = JWTManager(app)