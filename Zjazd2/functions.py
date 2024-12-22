import datetime

def prepare_file_name():
    now = datetime.datetime.now()
    return now.strftime('_%H%M%S')

users = {'Kamil': '123', 'Mario': 'M11'}
characters = set(',./;\'[]')
digits = set('0123456789')


def user_exist(login):
    if login in users.keys():
        return True
    else:
        return False

def password_correct(login, passwd):
    if users[login] == passwd:
        return True
    return False

def passwd_valid(passwd):
    counter = 0
    if passwd != passwd.upper():
        print('Znaleziono małą literę')
        counter += 1
    if passwd != passwd.lower():
        print('Znaleziono dużą literę')
        counter += 1
    if len(set(passwd) & characters) > 0:
        print('Znaleziono znak specjalny')
        counter += 1
    if len(set(passwd) & digits) > 0:
        print('Znaleziono cyfrę')
        counter += 1
    if counter == 4:
        return True
    return False

def add_user(login, passwd):
    users[login] = passwd
    print('Użytkownik dodany')


