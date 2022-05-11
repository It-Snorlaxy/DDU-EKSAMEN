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

def logincheck (logname):
    file = open('user_details.txt','rb')
    data = file.readlines()
    file.close()
    for i in data:
        i.replace(b'\n',b'')
        user, hashed, salt = i.split(b',', -1)
        if logname == user:
            logpass = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
            while True:
                if logpass == hashed:
                    print('Login succesful! Welcome')
                    return
                else:
                    print("password incorrect, try again")
                    logpass = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
    print("username not registered, try again")
    login()

def logreg():
    loginregist = input('log/reg? ')
    if loginregist == 'log':
        print('Du er ved at logge ind')
        login()
    elif loginregist == 'reg':
        register()
    else:
        logreg()

def login():
    logname = input('Navn: ').encode()
    logincheck(logname)


logreg()
