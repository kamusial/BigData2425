# program przyjmuje wiek i zarobki
# program reaguje na niepoprawne dane

while True:
    wiek = int(input('Podaj wiek: '))
    if 10 <= wiek <= 70:
        break
    elif wiek < 120:
        decision = input('Czy jestes pewny?: T/N')
        if decision.lower() == 't':
            break
    print('Niepoprawny wiek, jeszcze raz')

while True:
    wyplata = float(input('Ile zarabiasz?  '))
    if wyplata < 1000:
        print('niemozliwe, jeszcze raz')
    elif wyplata > 10000:
        print('zlodziej - jeszcze raz')
    else:
        break

print('Lecimy dalej')

