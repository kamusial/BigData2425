slowo = 'mamusia'
print(slowo)
print(slowo[3])   # 4ta litera
print(slowo[0])   # pierwsza litera
print(slowo[-1])  # ostatnia litera
print(slowo[2:5]) # znaki od 3go do 5go

counter_a = 0
for i in range(len(slowo)):
    print(f'iterator ma wartosc: {i}')
    print(f'Litera o indeksie {i} to {slowo[i]}')
    print()
    if slowo[i] == 'a':
        counter_a = counter_a + 1
print(f'Znalazlem {counter_a} liter a')
