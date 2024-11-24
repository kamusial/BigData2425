# uzytkownik wprowadza slowo
# komputer mówi, czy to palindrom, czy nie
# oko, kayak

text = input('podaj tekst: ')

# for i in range(len(text)):
#     if text[i] == text[-1-i]:

print(text[::-1])
if text.lower() == text[::-1].lower():
    print('Tak, to jest palindrom')

# dodatek: "Kobyła ma mały bok."



