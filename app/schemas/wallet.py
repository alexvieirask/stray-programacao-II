from services.config import *

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    balance = db.Column(db.Text, default = '00.00')    
    deposit = db.Column(db.Text, default = '00.00')