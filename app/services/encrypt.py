from hashlib import blake2b

''' Function that encrypt password '''
def encrypt_password(password):
    hash = blake2b()
    password_bytes = bytes(password, encoding= 'utf-8')
    hash.update(password_bytes)
    return hash.hexdigest() 

''' Compares whether the encrypted password is the same as the one provided '''
def authenticate_password(password_hash, password):
    get_encrypt_password = encrypt_password(password)
    
    
    if get_encrypt_password == password_hash:
        print (f'password authenticate:{ password }')
        return True
    else:
        print(f'password not authenticated:{ password }')
        return False


''' functions tests '''
PASSWORD = 'my-password'
encry_p = encrypt_password(PASSWORD)

''' The password provided is the same as the hash password  '''
print(f'First Test:')
authenticate_password(encry_p,'my-password')
print('-'*30)

''' The password provided is different from the hash password '''
print(f'Second Test:')
authenticate_password(encry_p,'MY-PASSWORD')