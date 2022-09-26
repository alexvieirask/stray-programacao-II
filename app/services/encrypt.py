from hashlib import blake2b
import random
from schemas.giftcard import *


''' this func '''
def encrypt_password(password):
    hash = blake2b()
    password_bytes = bytes(password, encoding= 'utf-8')
    hash.update(password_bytes)
    return hash.hexdigest() 

''' this func '''
def authenticate_password(password_hash, password):
    get_encrypt_password = encrypt_password(password)
    if get_encrypt_password == password_hash:
        return True
    else:
        return False

''' this func '''
def giftcard_generator():
    LETTERS_AND_NUMBERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    giftcard_code = ''
    for index in range(3):    
        TOKEN = ''.join(random.sample(LETTERS_AND_NUMBERS,4))  
        giftcard_code += TOKEN 
        if index < 2: 
            giftcard_code += '-' 
    return giftcard_code