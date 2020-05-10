import random
import time
import string
import subprocess
from pyfiglet import Figlet
subprocess.run(["clear"])
t = time.sleep
s = string
f = Figlet(font='tty')
print(f.renderText('PASSWORD GENERATOR'))
#title = ['passkey generator',
#         'Passkey generator',
#         'PAsskey generator',
#         'PASskey generator',
#         'PASSkey generator',
#         'PASSKey generator',
#         'PASSKEy generator',
#         'PASSKEY generator',
#         'PASSKEY Generator',
#         'PASSKEY GEnerator',
#         'PASSKEY GENerator',
#         'PASSKEY GENErator',
#         'PASSKEY GENERator',
#         'PASSKEY GENERAtor',
#         'PASSKEY GENERATor',
#         'PASSKEY GENERATOr',
#         'PASSKEY GENERATOR']
#
## clear screen and display title
#os.system('clear||cls')
#t(1)
#for i in title:
#    t(.03)
#    os.system('clear||cls')
#    print(i)
#    print "\n"

# display password options
a = ['1. 8 CHAR PASSKEY',
     '2. 12 CHAR PASSKEY',
     '3. 16 CHAR PASSKEY',
     '4. Hard-core',
     '5. <shift> PASSKEY']
for i in a:
    print(i)
    continue
    print("\n")

# variable to generate characters for options 1 - 4
char_set = s.ascii_letters + s.digits + s.punctuation 
select = input('-> ')

while(select != '1' and select != '2' and select != '3' and select != '4' and select != '5'):
    select = input('select 1 - 5: ')

### password option 1
### log passwords to file 

if select == '1':
    x8_characters = ''.join(random.sample(char_set*8, 8))
    print(x8_characters)
    
    logfile = input('save to logfile? y or n: ')
    
    while(logfile != 'y' and logfile != 'n'):
        logfile = input('enter y or n: ')

    if logfile == 'y':
        filepath = input('enter file path to logfile: ')
        log = open(filepath, 'a')
        log.write(x8_characters + '\n')
        log.close()
    if logfile == 'n':
        pass

### password option 2

elif select == '2':
    x12_characters = ''.join(random.sample(char_set*12, 12))
    print(x12_characters)

    logfile = input('save to logfile? y or n: ')
    
    while(logfile != 'y' and logfile != 'n'):
        logfile = input('enter y or n: ')

    if logfile == 'y':
        filepath = input('enter file path to logfile: ')
        log = open(filepath, 'a')
        log.write(x12_characters + '\n')
        log.close()
    if logfile == 'n':
        pass


### password option 3

elif select == '3':
    x16_characters = ''.join(random.sample(char_set*16, 16))
    print(x16_characters)
    logfile = input('save to logfile? y or n: ')
    
    while(logfile != 'y' and logfile != 'n'):
        logfile = input('enter y or n: ')
    
    if logfile == 'y':
        filepath = input('enter file path to logfile: ')
        log = open(filepath, 'a')
        log.write(x16_characters + '\n')
        log.close()
    if logfile == 'n':
        pass


### password option 4

elif select == '4':
    hardcore = ''.join(random.sample(char_set*20, 20))
    print(hardcore)
    logfile = input('save to logfile? y or n: ')

    while(logfile != 'y' and logfile != 'n'):
        logfile  = input('enter y or n: ')

    if logfile == 'y':
        filepath = input('enter file path to logfile: ')
        log = open(filepath, 'a')
        log.write(hardcore + '\n')
        log.close()
    if logfile == 'n':
        pass


elif select == '5':

    # option 5 generates passwords to be typed while holding the shift key.
    # used for the convenience of having complex passwords while
    # making them quicker/easier to type and/or remember.
    # list of shift key symbols.
    # assign all uppercase letters to variable.
    # concatenate string of uppercase letters to list of symbols.
    # user input to choose number of characters in password
    shift_sets = ['1. 8 key shift set',
                  '2. 12 key shift set',
                  '3. 16 key shift set']
    for i in shift_sets:
        print(i)
        continue

    shift = ['~','!','@','#','$','%','^',
             '&','*','(',')','_','+','{',
             '}','|',':','"','<','>','?']

    shift2 = string.ascii_uppercase
    shift.extend(shift2)
    
    select2 = input('--> ')

    while(select2 != '1' and select2 != '2' and select2 != '3'):
        select2 = input('enter 1 - 3: ')

    if select2 == '1':
        shift_8 = ''.join(random.sample(shift*8, 8))
        print(shift_8)
        logfile = input('save to logfile? y or n: ')

        while(logfile != 'y' and logfile != 'n'):
            logfile = input('enter y or n: ')
        
        if logfile == 'y':
            filepath = input('enter file path to logfile: ')
            log = open(filepath, 'a')
            log.write(shift_8 + '\n')
            log.close()
        if logfile == 'n':
            pass


    elif select2 == '2':
        shift_12 = ''.join(random.sample(shift*12, 12))
        print(shift_12)
        logfile = input('save to logfile? y or n: ')

        while(logfile != 'y' and logfile != 'n'):
            logfile = input('enter y or n: ')
        
        if logfile == 'y':
            filepath = input('enter file path to logfile: ')
            log = open(filepath, 'a')
            log.write(shift_12 + '\n')
            log.close()
        if logfile == 'n':
            pass


    elif select2 == '3':
        shift_16 = ''.join(random.sample(shift*16, 16))
        print(shift_16)
        logfile = input('save to logfile? y or n: ')

        while(logfile != 'y' and logfile != 'n'):
            logfile = input('enter y or n: ')

        if logfile == 'y':
            filepath = input('enter file path to logfile: ')
            log = open(filepath, 'a')
            log.write(shift_16 + '\n')
            log.close()
        if logfile == 'n':
            pass

    else:
        pass
else:
    pass
