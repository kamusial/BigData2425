password = '1234'

while True:
    user_passwd = input('Wprowadz haslo:   ')
    if user_passwd == password:
        break
    elif user_passwd == 'Kamil':
        nazwisko = input('Podaj nazwisko Kamila:   ')
        if nazwisko == 'Musial':
            pesel = int(input('Podaj pesel:'))
            if pesel == 1234:
                break

print('Witamy w programie')