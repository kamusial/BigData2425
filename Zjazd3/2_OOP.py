# kasa reprezentująca konto bankowe

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Konto należy do {self.owner} i jest na nim {self.balance} kasy'

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Poprawna wpłata\naktuale saldo: {self.balance}')
        else:
            print('Wpłacana kwota musi być dodatnia')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f' Wypłata: {amount}\nzostało: {self.balance}')
        else:
            print(f'Niewystaeczajace środki\nmożna wypłać do {self.balance}')

    def display_balance(self):
        self.balance -= 1
        print('Pobrano 1zł za sprawdzenie')
        print(f'Konto: {self.owner}, saldo: {self.balance}')


# tworzenie kont
konto1 = BankAccount('Kamil', 1000)
konto2 = BankAccount('Ada')

# operacje
konto1.display_balance()
konto1.display_balance()
konto1.deposit(500)
konto1.withdraw(200)
konto1.display_balance()

konto2.display_balance()
konto2.deposit(300)
konto2.withdraw(300)
konto2.display_balance()

print(konto2)