''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Esquema: [ User ]
    descrição: 
'''
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable = False, unique= True)
    email = db.Column(db.Text, nullable=False, unique= True)
    password = db.Column(db.Text, nullable=False)
    wallet = db.Column(db.Float, default = 0)
    description = db.Column(db.Text)
    profile_picture = db.Column(db.Text)
    registration_date = db.Column(db.DateTime, default= datetime.now())
    is_admin = db.Column(db.Boolean, default=False)
    
    medals = db.relationship(Medal, backref= "User")
    purchases = db.relationship(Purchase, backref = "User") 
    giftcards = db.relationship(GiftCard, backref = "User")
    
    def json(self) -> dict:
        return { 
            "id": self.id,
            "name": self.name,
            "username":self.username,
            "e-mail": self.email, 
            "password": self.password,
            "wallet": self.wallet,
            "description": self.description,
            "profile_picture" : self.profile_picture,
            "registration_date": self.registration_date,
            "is_admin": self.is_admin
        }
    

    def validate_login(username:str,password:str) -> bool:
        ''' Essa função realiza a verificação do login. \n Return: bool  '''
        user = db_query_by_username(User, username)
        if user:
            password = check_password_hash(user.password,password)
            if password:
                return True
        return False