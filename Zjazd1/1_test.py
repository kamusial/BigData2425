print('Siema')
wiek = int(input('Ile masz lat?   '))

if wiek <= 0:
    print('niemozliwe')
elif wiek < 18:
    print(f'Bedziesz dorosly za {18 - wiek} lat')
    print('I ok')
elif wiek <= 21:
    print('Mlody dorosly')
elif wiek == 21:
    print('Dokladnie teraz osiagnales dorososc w USA')
else:
    print('Jestes dorosly')

print('Dalsza czesc programu')
