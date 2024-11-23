# mamy listę aut do wynajecia:
cars = ['Audi', 'BMW', 'Toyota', 'Ford']

# program ma 2 funkcje
# można wybrać model auta
# można dodać model do listy
# program pyta, kiedy wyjść z programu

while True:
    my_car = input('podaj model auta: ')
    if my_car in cars:
        print(f'Wybrales {my_car}')
    else:
        cars.append(my_car)
    decission = input('czy chcesz sprawdzic kolejny auto?  T/N ')
    if decission.lower() != 't':
        break

print('Koniec')