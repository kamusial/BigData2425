# program, który pyta o dane uzytkownika
# program pyta, czy wpisać kolejnego użytkownika
# program zapisuje wszystkie dane
# użytkownikom pełnoletnim program generuje numer ID


users_list = []
user_tmp = []

while True:
    first_name = input('Podaj imie:   ')
    last_name = input('Podaj nazwisko:   ')
    age = int(input('Podaj wiek:   '))
    user_tmp.append(first_name)
    user_tmp.append(last_name)
    user_tmp.append(age)
    if age >= 18:
        user_tmp.append(1234)
    else:
        user_tmp.append(None)

    print(f'użytkownik {user_tmp} zapisany')
    users_list.append(user_tmp)
    user_tmp = []
    decission = input('Czy chcesz dodać kolejnego użytkownika?  T/N   ')
    if decission[0].lower() == 't':
        print('Ok, dodaj kolejną osobę')
    elif decission[0].lower() == 'n':
        print('Ok, koniec dodawania osób')
        break
    else:
        print('Nierozpoznany wobór, jeszcze raz')
        decission[0] = input('Czy chcesz dodać kolejnego użytkownika?  T/N   ')
        if decission.lower() == 't':
            print('Ok, dodaj kolejną osobę')
        else:
            print('koniec dodawania osób')
            break

print(f'Użytkownicy: {users_list}')

