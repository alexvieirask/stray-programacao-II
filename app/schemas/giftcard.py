from enum import unique
from services.config import *

''' Class Giftcard:  desc. '''

class GiftCard(db.Model):
    __tablename__ = 'GiftCard'
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Integer)
    giftcard_code = db.Column(db.Text, unique = True)
    available = db.Column(db.Boolean, default= True)


    ''' this function return datas in JSON format '''
    def json(self):
        return {
            "id:": self.id,
            "value": self.value,
            "giftcard_code": self.giftcard_code,
            'available': self.available
        }