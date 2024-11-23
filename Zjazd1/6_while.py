password = '1234'

user_passwd = input('Wprowadz haslo:   ')

while user_passwd != password:
    print('zle haslo')
    user_passwd = input('Wprowadz haslo:   ')

print('haslo przyjete')
