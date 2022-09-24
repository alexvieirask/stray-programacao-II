from services.config import *

''' Class Library:  desc. '''
class GiftCard(db.Model):
    __tablename__ = 'GiftCard'
    id = db.Column(db.Integer, primary_key=True)
    pass
    
    ''' this function return datas in JSON '''
    def json(self):
        return {
            "id": self.id
         
        }