from services.config import *
from services.encrypt import *



''' Class User:  desc. '''

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable = False, unique= True)
    email = db.Column(db.Text, nullable=False, unique= True)
    password = db.Column(db.Text, nullable=False)
    age = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text)
    profile_picture = db.Column(db.Text)
    registration_date = db.Column(db.DateTime, default= datetime.now())
    is_admin = db.Column(db.Boolean, default=False)

    ''' this function return datas in JSON format '''
    def json(self):
        return { 
            "id": self.id,
            "name": self.name,
            "username":self.username,
            "e-mail": self.email, 
            "password": self.password,
            "age": self.age,
            "description": self.description,
            "profile_picture" : self.profile_picture,
            "registration_date": self.registration_date,
            "is_admin": self.is_admin
        }