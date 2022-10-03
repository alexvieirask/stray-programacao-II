from services.config import *
from services.encrypt import *
from schemas.medal import Medal
from schemas.purchase import Purchase

''' User Schema:    

atributes:
    id: Integer
    username: Text
    e-mail: Text
    password: Text
    wallet: Text
    description: Text
    profile_picture: Text
    registration_date : DateTime <Default value: datetime.now()>
    is_admin : Boolean <Default value: false>
'''

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable = False, unique= True)
    email = db.Column(db.Text, nullable=False, unique= True)
    password = db.Column(db.Text, nullable=False)
    wallet = db.Column(db.Text, default = '0')
    description = db.Column(db.Text)
    profile_picture = db.Column(db.Text)
    registration_date = db.Column(db.DateTime, default= datetime.now())
    is_admin = db.Column(db.Boolean, default=False)
    
    medals = db.relationship(Medal, backref='User')
    purchases = db.relationship(Purchase, backref = 'User') 
    

    ''' this function return datas in JSON format '''
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
    
    ''' this func '''
    def create_user ( name:str,username:str, email:str, password:str, wallet:str,  
                    description:str, profile_picture:str) -> tuple:
        try:
            
            hash_password = encrypt_password(password)

            new_user = User(
                name = name, 
                username = username, 
                email = email, 
                password = hash_password, 
                wallet = wallet, 
                description = description, 
                profile_picture = profile_picture
            )    
            
            db.session.add(new_user)
            db.session.commit()
            return 200, new_user.json()

        except Exception as error:
            return str(error)
    
    def delete_user (id) -> tuple:
        try:
            user = User.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return 200, user.json()

        except Exception as error:
            return str(error)

    def return_user_by_id(id):
        try:
            user = User.query.get(id)
            return 200, user.json()
        
        except Exception as error:
            return str(error)

    def return_all_users() -> tuple:
        try:
            users = User.query.all()
            json_users = [ user.json() for user in users ]
            return 200, json_users

        except Exception as error:
            return str(error) 

    def default_users_add(users:list) -> int:
        try:
            for user in users:
                db.session.add(user)
            db.session.commit()
            return 200
        
        except Exception as error:
            return str(error)
    
    def return_all_purchases_user(id:int) -> tuple:
        try:
            purchases = User.query.get(id).purchases
            return 200, purchases

        except Exception as error:
            return str(error)