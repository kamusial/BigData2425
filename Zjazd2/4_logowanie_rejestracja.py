# import functions
from functions import *

login = input('Podaj login:   ')
passwd = input('Podaj hasło:   ')

if user_exist(login) and password_correct(login, passwd):
    print('użytkownik zalogowany')




else:
    print(f'Rejestracja {login}')
    users[login] = passwd


special_caracters = {',.;/\\\'[]'}
len(set(passwd) & special_caracters)

