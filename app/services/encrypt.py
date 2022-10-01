from hashlib import blake2b
import random


''' this func '''
def encrypt_password(password) -> str:
    hash = blake2b()
    password_bytes = bytes(password, encoding= 'utf-8')
    hash.update(password_bytes)
    return hash.hexdigest() 

''' this func '''
def authenticate_password(password_hash, password) -> bool:
    get_encrypt_password = encrypt_password(password)
    if get_encrypt_password == password_hash:
        return True
    else:
        return False

''' this func '''
def giftcard_generator() -> str:
    LETTERS_AND_NUMBERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    token_generate = ''
    
    for item in range(3):
        TOKEN = ''.join(random.sample(LETTERS_AND_NUMBERS,4))
        token_generate += TOKEN 
        if item < 2:
            token_generate += '-' 
    return(token_generate)