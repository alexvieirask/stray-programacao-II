''' Importações extras '''
from datetime import datetime, timedelta
import os
import random

''' Configuração do nome do arquivo da database  '''
extension = ".db"
filename = "database"
database_file = filename + extension

''' Importações Flask SQLALCHEMY '''
from flask import Flask, render_template,jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt,generate_password_hash,check_password_hash
from sqlalchemy.exc import IntegrityError

''' Configurações Flask SQLALCHEMY '''
app = Flask(__name__, template_folder='../src', static_folder='../src/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.session.execute('pragma foreign_keys=on')

''' Importações JWT '''
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

''' Configurações JWT '''
app.config["JWT_SECRET_KEY"] = "faf1644b1743243a99f051f223464a66bdd665c2389b519f0d1d2a90c32efb6b"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
jwt = JWTManager(app)

cors = CORS(app)
bcrypt = Bcrypt(app) 

''' Importações Esquemas '''
from schemas.medal import Medal
from schemas.purchase import Purchase
from schemas.giftcard import GiftCard
from schemas.screenshot import Screenshot
from schemas.game import Game
from schemas.user import User

''' Criação da database '''
if not os.path.exists(database_file):
    db.create_all()