def prepare_pc():
    print('Resetowanie dysku')
    print('Wgrywanie company portal')
    print('Weryfikacja uprawnień')
    print('Hej, witamy w firmie')


prepare_pc()
prepare_pc()
prepare_pc()



def welcome1(name):
    print(f'welcome {name}')


def welcome2(name, age):
    if age < 18:
        print(f'cześć {name}')
    else:
        if name[-1] == 'a':
            print(f'Witam Pani {name}')
        else:
            print(f'Witam Pana {name}')


def health_check(age, sex, height, weight, smoking):
    result = 0
    if sex == 'f':
        result += 1
    if age < 50:
        result += 2
    if weight / (height / 100 ** 2) < 30:
        result += 2
    if smoking:
        result -= 2
    return result


if health_check(44, 'm', 180, 94, False) > 3:
    print('Gratulacje, możesz być ubezpieczony')


