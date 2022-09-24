from services.config import *

''' Class User:  desc. '''
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable = False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    registration_date = db.Column(db.DateTime, default= datetime.now())
    is_admin = db.Column(db.Boolean, default=False)

    ''' this function return datas in JSON '''
    def json(self):
        return { 
            "id": self.id,
            "username":self.username,
            "e-mail": self.email, 
            "password": self.password,  
            "registration_date": self.registration_date,
            "is_admin": self.is_admin
        }