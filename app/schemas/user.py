from services.config import *
from services.encrypt import *


''' User Schema:

atrr:
    id: Integer
    username: Text
    e-mail: Text
    password: Text
    registration_date : DateTime <Default value: datetime.now()>
    is_admin : Boolean <Default value: false>

functions: 
    create_user
    delete_user
    return_all_users
    return_user_by_id
    default_users_add
'''

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
    def json(self) -> dict:
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
    
    ''' this func '''
    def create_user ( name:str,username:str, email:str, password:str, age:str, description:str, profile_picture:str) -> tuple:
        try:
            USER = User(name = name, username = username, email = email, 
            password = encrypt_password(password), age = age, 
            description = description, profile_picture = profile_picture)    
            
            db.session.add(USER)
            db.session.commit()
            return 200, USER.json()

        except Exception as error:
            return str(error)
    
    ''' this func '''
    def delete_user (id) -> tuple:
        try:
            USER = User.query.get(id)
            db.session.delete(USER)
            db.session.commit()
            return 200, USER.json()

        except Exception as error:
            return str(error)


    ''' this func '''
    def return_user_by_id(id):
        try:
            USER = User.query.get(id)
            return 200, USER.json()
        
        except Exception as error:
            return str(error)


    ''' this func '''
    def return_all_users() -> tuple:
        try:
            USERS = User.query.all()
            json_users = [ user.json() for user in USERS ]
            return 200, json_users

        except Exception as error:
            return str(error) 


    '''this func'''
    def default_users_add(users:list) -> int:
        try:
            for user in users:
                db.session.add(user)
            db.session.commit()
            return 200
        
        except Exception as error:
            return str(error)
    
    '''this func'''
    def return_all_purchases_user(id:int) -> tuple:
        try:
            PURCHASES = User.query.get(id).purchases
            return 200, PURCHASES

        except Exception as error:
            return str(error)