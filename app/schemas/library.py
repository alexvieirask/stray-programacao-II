from services.config import db

''' Class Library:  desc. '''
class Library(db.Model):
    __tablename__ = 'Library'
    id = db.Column(db.Integer, primary_key=True)
    pass

    ''' this function return datas in JSON '''
    def json(self):
        return {
            "id": self.id
        }