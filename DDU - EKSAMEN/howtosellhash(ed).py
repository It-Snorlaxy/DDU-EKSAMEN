import bcrypt
import hashlib


def register ():
    salt = bcrypt.gensalt()
    print('Making a user')
    regname = input('Name: ').encode()
    usercheck(regname)
    hashed = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
    file = open('user_details.txt','ab')
    file.write(regname + b',' + hashed + b',' + salt + b'\n')
    file.close()
    logreg()

def logincheck (logname):
    print('login')
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
        print('Loggin in')
        login()
    elif loginregist == 'reg':
        register()
    else:
        logreg()

def login():
    logname = input('Name: ').encode()
    logincheck(logname)

def usercheck(regname):
    file = open('user_details.txt', 'rb')
    data = file.readlines()
    file.close()
    for i in data:
        i.replace(b'\n',b'')
        user, hashed, salt = i.split(b',', -1)
        if regname == user:
            print('user already exists, try a new one')
            register()


logreg()
