data = input('Wprowadz daną: ')
try:
    data = int(data)
    print('Zamieniono na int')
except:
    try:
        data = float(data)
        print('Zamieniono na float')
    except:
        print('Zostaje string')
