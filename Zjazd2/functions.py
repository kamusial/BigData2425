users = {'Kamil': '123', 'Mario': 'M11'}


def user_exist(login):
    if login in users.keys():
        return True
    else:
        return False

def password_correct(login, passwd):
    if users[login] == passwd:
        return True
    return False