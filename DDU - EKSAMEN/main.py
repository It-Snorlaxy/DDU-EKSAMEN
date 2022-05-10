import bcrypt
import hashlib
LR = None

#generating salt
salt = bcrypt.gensalt()

#somehting
def register ():
    print('Making a user')
    user = input('Navn: ')
    file.write(user + ',' + str(hashed) + ',' + str(salt) + '\n')
    file = open('user_details.txt','ab')
    file.write(user + b',' + hashed + b',' + salt + b'\n')
    file.close()
    logreg()

def login (logname, logpass):
    file = open('user_details.txt','rb')
    for i in file:
        user, heashed, salt = i.split(b',')
    bcrypt.checkpw(logpass, hashed)
    file.close()

def logreg():
    loginregist = input('log/reg? ')
    if loginregist == 'log':
        print('Du er ved at logge ind')
        logname = input('Navn: ').encode()
        logpass = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
        login(logname, logpass)
    elif loginregist == 'reg':
        register()
    else:
        logreg()
logreg()
