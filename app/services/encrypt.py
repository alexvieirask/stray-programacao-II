
import random

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