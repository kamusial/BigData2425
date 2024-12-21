class Auto:
    def __init__(self,color, year):
        self.color = color
        self.condition = 5
        self.mileage = 0
        self.age = 2024 - year

    def change_mileage(self, km):
        if km >= 0:
            self.mileage += km
        else:
            passwd = input('podaj haslo serwisowe:  ')
            if passwd == '1234':
                print('Zaraportowano')
                self.mileage += km



auto11 = Auto()
auto12 = Auto()
print(auto11.color)
auto11.color = 'red'
auto12.mileage += 100
print(auto11.color)
