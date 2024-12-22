# import functions
from functions import *

while True:
    decission = input('Logowanie bądź Rejestracja  L / R:  ')
    if decission[0].lower() == 'l':
        login = input('Podaj login:   ')
        passwd = input('Podaj hasło:   ')
        if user_exist(login) and password_correct(login, passwd):
            print('użytkownik zalogowany')
            break
        else:
            print('Login bądź hasło niepoprawne')
    elif decission[0].lower() == 'r':
        login = input('Podaj login:   ')
        if not user_exist(login):
            passwd1 = input('Podaj haslo: ')
            passwd2 = input('Potwierdź haslo: ')
            if passwd1 == passwd2:
                if passwd_valid(passwd1):
                    add_user(login, passwd1)
                    break
    else:
        print('Niepopranwy wybór')



