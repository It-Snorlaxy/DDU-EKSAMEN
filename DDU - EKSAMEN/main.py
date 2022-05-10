import os
import bcrypt
import hashlib

salt = b'$2b$12$8gppykpvjYHUlqNeJXvI7e'

def register ():
    global N_user
    N_user = input('Name: ').encode()
    if os.stat("user_details.txt").st_size == 0:
        hashed = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
        file = open('user_details.txt','ab')
        file.write(N_user + b',' + hashed + b',' + salt + b'\n')
        file.close()
        logreg()
    else:
        Usernamecheck()

    while U_passed == True:
        hashed = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
        file = open('user_details.txt','ab')
        file.write(N_user + b',' + hashed + b',' + salt + b'\n')
        file.close()
        logreg()
    else:
        print('Whoops that username is already in use')
        register()

def Usernamecheck():
    global U_passed
    with open('user_details.txt','rb') as file:
        for line in file:
            user, hashed, salt = line.split(b',')
            if N_user == user:
                U_passed = False
                break
            else:
                U_passed = True
    file.close()

def logincheck (logname, logpass):
    with open('user_details.txt','rb') as file:
        for line in file:
            user, hashed, salt = line.split(b',')
            if logname == user and logpass == hashed:
                print('Login succesful! Welcome')
                file.close()
                exit()
            else:
                pass
        print("username or password is incorrect, try again")
        login()
    file.close()

def logreg():
    loginregist = input('log/reg? ')
    if loginregist == 'log':
        print('Du er ved at logge ind')
        login()
    elif loginregist == 'reg':
        print('Making a user')
        register()
    else:
        logreg()

def login():
    logname = input('Name: ').encode()
    logpass = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
    logincheck(logname, logpass)


logreg()
