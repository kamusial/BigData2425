# dana jest lista uzytkowniów
# program rejetruje nwoego uzytkownika i zapętla się, gdy dany użytkownik jest już w bazie
# program wita inaczej Oanów i Panie

users = ['Kamil', 'Anna01', 'piesek', 'DIDI']

while True:
    name = input('Podaj nazwe:   ')
    if name not in users:
        users.append(name)
        break
    else:
        print('Nazwa istnieje, podaj inną')

if name[-1].lower() == 'a':
    print('Witam Panią')
else:
    print('Witam Pana')

