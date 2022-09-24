from services.config import db

''' Class Wallet:  desc. '''
class Wallet(db.Model):
    __tablename__ = 'Wallet'
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Numeric, default = 00.00)     

    ''' this function return datas in JSON '''
    def json(self):
        return { 
            "id": self.id,
            "balance": self.balance      
        }