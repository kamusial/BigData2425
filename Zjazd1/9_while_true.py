# gra. Program losuje liczbe.
# uzytkownik zgaduje liczbe, a program informuje, czy
# liczba dana przez uzytkownika jest ok, za duza, czy za mała

import random
wylosowana_liczba = random.randint(0, 100)
while True:
    liczba = int(input('Zgadnij liczbe:   '))
    if liczba == 9999:
        passwd = input('Podaj haslo')
        if passwd == '':
            print(f'Liczba wynosi okolo: {round(wylosowana_liczba / 10)*10}')
    elif liczba > wylosowana_liczba:
        print('Za duzo')
    elif liczba < wylosowana_liczba:
        print('Za malo')
    else:
        break
