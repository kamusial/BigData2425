class Auto:
    def __init__(self, color, year):
        self.color = color
        self.condition = 5
        self.mileage = 0
        self.age = 2025 - year

    def change_mileage(self, km):
        if km >= 0:
            self.mileage += km
        else:
            passwd = input('podaj haslo serwisowe:  ')
            if passwd == '1234':
                print('Zaraportowano')
                self.mileage += km


auto11 = Auto('red', 2021)
auto12 = Auto('blue', 1999)
print(auto11.color)
auto11.color = 'white'
auto12.mileage += 100
print(auto11.color)
