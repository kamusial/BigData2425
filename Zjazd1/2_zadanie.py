# program pyta o zarobki i liczbe dzieci
# na dziecko jest 800+
# program zwraca kwote na głowę w rodzinie

# 800+ jest na 3cie i kolejne dziecko
# jeśli oboje rodzice razem zarabiają powyżej 10k
# płacą dodatkowy podatek

liczba_dzieci = int(input('Ile masz dzieci?   '))
zarobki = int(input('Ile zarabiasz?   '))
if liczba_dzieci > 2:
    print(f'Na osobe {round((zarobki + (liczba_dzieci-2)*800)/(liczba_dzieci + 2),2)}')
else:
    total = zarobki + liczba_dzieci * 800
    kasa_na_glowe = total / (liczba_dzieci + 2)
    print(f'Na osobe w rodzinie: {kasa_na_glowe}')
