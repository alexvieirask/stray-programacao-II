from services.config import *
from services.encrypt import encrypt_password
from schemas.user import User

''' User Schema:

atrr:
    id: Integer
    username: Text
    e-mail: Text
    password: Text
    wallet: Text <Default value: 0>
    registration_date : DateTime <Default value: datetime.now()>
    is_admin : Boolean <Default value: false>

functions: 
    create_user
    delete_user
    return_all_users
    return_user_by_id
    default_users_add
'''

''' this func '''
def create_user ( name:str,username:str, email:str, password:str, wallet:str, age:str, description:str, profile_picture:str ):
    try:
        USER = User(name = name, username = username, email = email, 
        password = encrypt_password(password),wallet = wallet, age = age, 
        description = description, profile_picture = profile_picture)    
        
        db.session.add(USER)
        db.session.commit()
        return 200

    except Exception as error:
        return str(error)


''' this func '''
def delete_user (id):
    try:
        USER = User.query.get(id)
        db.session.remove(USER)
        db.session.commit()

    except Exception as error:
        return str(error)



''' this func '''
def return_user_by_id(id):
    try:
        USER = User.query.get(id)
        print(USER.json())
        return 200
    
    except Exception as error:
        return str(error)

def return_all_users():
    try:
        USER = User.query.all()
        
        for user in USER:
            print(user.json())
        return 200

    except Exception as error:
        return str(error)

