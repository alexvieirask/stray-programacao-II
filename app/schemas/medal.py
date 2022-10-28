''' Importação das configurações  '''
from services.config import *
from services.utils import *

''' Esquema: [ Medal ]
    descrição: Esquema de Medal utilizado no sistema.
'''
class Medal(db.Model):
    __tablename__ = 'Medal'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    icon = db.Column(db.Text, nullable = False)
    received_date = db.Column(db.DateTime, default= datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
     
    def json(self) -> dict:
        return  {
            "id": self.id,
            "title": self.title,
            "description" : self.description,
            "received_date" :  self.received_date
        }
