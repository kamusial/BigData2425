zakupy = ['mleko', 'sok', 'chleb', 'serek', 'czekolada']
print(zakupy)
print(zakupy[0])
print(zakupy[3])
print(zakupy[-1])
print(zakupy[1:4])
print(zakupy[0:5])
print(f'lista zakupow ma {len(zakupy)} elementow')

counter = 0
for i in range(len(zakupy)):
    print(zakupy[i])
    if len(zakupy[i]) > 5:
        print(f'produkt {zakupy[i]} ma wiecej niz 5 liter')
        counter = counter + 1
print(counter)

men = []
women = []
imiona = ['Kamil', 'Kamil', 'Julia', 'Mikolaj', 'Marcin', 'Anna']
for i in range (len(imiona)):
    if imiona[i][-1] == 'a':   # ostatnia litera elementu listy
        print(f'{imiona[i]} to imie zenskie')
        women.append(imiona[i])
    else:
        print(f'{imiona[i]} to imie meskie')
        men.append(imiona[i])

for imie in imiona:
    if imie[-1] == 'a':
        women.append(imie)
    else:
        men.append(imie)


