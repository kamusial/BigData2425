# program, który pyta o dane uzytkownika
# program pyta, czy wpisać kolejnego użytkownika
# program zapisuje wszystkie dane
# użytkownikom pełnoletnim program generuje numer ID


user = []
first_name = input('Podaj imie:   ')
last_name = input('Podaj nazwisko:   ')
age = input('Podaj wiek:   ')
user.append(first_name)
user.append(last_name)
user.append(age)

print(f'użytkownik {user} zapisany')
user[2]