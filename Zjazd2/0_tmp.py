def mnozenie(a, b):
    result = round(a * b, 6)  # zaokrąglenie do 6 miejsc po przecinku
    return result


print('Witamy w programie')
# wynik = mnozenie(2, 3)
print(f'wynik wynosi {mnozenie(100, 1.1)}')
print(f'wynik wynosi {mnozenie(0.1, 0.2)}')


# funkcja przyjmuje dane o uzytkowniu
# i zwracam stawke ubezpieczenia


def insurance_payment(age, bmi, smoking, health_level=5):
    total = 100
    total += age * 1.3
    if bmi > 30:
        total += bmi * .9
    if smoking == 't':
        total *= 2
    total += (5-health_level) * 12.3
    return total


print(f'Ubezpieczenie Kowalski: {insurance_payment(54, 22, "n")}')





