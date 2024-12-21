users = {'Kamil': '123', 'Mario': 'M11'}

login = input('Podaj login:   ')
passwd = input('Podaj hasło:   ')
if login in users.keys():
    if passwd == users[login]:
        print('Zalogowany')
    else:
        exit()
else:
    print(f'Rejestracja {login}')
    users[login] = passwd


special_caracters = {',.;/\\\'[]'}
len(set(passwd) & special_caracters)

