my_dict = {'imie': 'Kamil', 'wiek': 30, 'skill': 3.5, 'wiek': 25}

print(my_dict)
print(my_dict['wiek'])

my_dict['wiek'] += 2
print(my_dict['wiek'])
my_dict['waga'] = 85

shopping_list = {}

while True:
    product = input('Co chcesz kupić?  ')
    quantity = input('Ile?  ')
    shopping_list[product] = quantity
    if product in shopping_list.keys():
        shopping_list[product] += quantity
    else:
        shopping_list[product] = quantity
    decission = input('Czy chcesz dodać kolejny produkt?  ')
    if decission.lower() != 't':
        break

print(shopping_list)
print(shopping_list.items())
print(shopping_list.keys())
print(shopping_list.values())

