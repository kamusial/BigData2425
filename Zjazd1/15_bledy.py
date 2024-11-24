while True:
    try:
        age = int(input('Podaj wiek: '))
        break
    except:
        print('Nie udało się odczytać wieku, jako liczby')
        print('Przyjmuje wiek 18 lat')


print(f'przejdziesz na emerytuje za {65 - age}')



