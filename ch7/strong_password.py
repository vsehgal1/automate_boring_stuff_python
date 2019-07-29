# strong_password.py
# automatetheboringstuff.com Chapter 7
# Vikram Sehgal

import re

def str_pass(passw):
    reg_dig = re.compile(r'\d') #regex for digits
    reg_upper = re.compile(r'[A-Z]')  #regex for uppercase
    reg_lower = re.compile(r'[a-z]')  #regex for lowercase
    
    if len(passw) >= 8:  #check password length
	#check if either case (upper, lower, digits) is false
        if reg_dig.search(passw) == None:
            return False
        elif reg_lower.search(passw) == None:
            return False
        elif reg_upper.search(passw) == None:
            return False
        else: return True

    else: return False


if __name__ == '__main__':
    passw = input('Input password: ')
    if str_pass(passw) == True:
        print('Strong Password')

    else: print('Weak password')
