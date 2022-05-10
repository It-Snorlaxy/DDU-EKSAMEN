import bcrypt
import hashlib
LR = None

salt = bcrypt.gensalt()

def register ():
    print('Making a user')
    user = input('Navn: ')
    hashed = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
    file = open('user_details.txt','a')
    file.write(user + ',' + str(hashed) + ',' + str(salt) + '\n')
    file.close()
    logreg()

def login (logname, logpass):
    file = open('user_details.txt','r')
    for i in file:
        user, hashed, salt = i.split(',')
    bcrypt.checkpw(logpass, hashed)
    file.close()

def logreg():
    loginregist = input('log/reg? ')
    if loginregist == 'log':
        print('Du er ved at logge ind')
        logname = input('Navn: ')
        logpass = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
        login(logname, logpass)
    elif loginregist == 'reg':
        register()
    else:
        logreg()
