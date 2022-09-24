from services.config import *
from schemas.user import  User


''' user create'''
USER = User( username = "LiLCrazzyFN", email = "alexvieiradias@gmail.com", password = "47 99018 3232")

''' data persistent '''
db.session.add(USER)
db.session.commit()