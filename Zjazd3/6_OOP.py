"Program OOP do analizy danych sprzedażowych"

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(ID: {self.product_id}, Name: {self.name}, Price: {self.price})"


class SalesDataL:    # zarządzanie danymi sprzedaży
    def __init__(self):
        self.sales = []

    def add_sale(self, product, quantity):
        self.sales.append({'produkt': product, "quantity": quantity})

    def get_all_sales(self):
        return self.sales

class  SalesAnalysis:    # analiza danych
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def revenue(self):
        # oblicz całkowity przychów
        return sum(sale['product'].price * sale['quantity'] for sale in self.sales_data.get_all_sales())


    def best_selling_product(self):
        # najlepie sprzedający się produkt

    def sales_summary(self):
        # podsumowanie sprzedaży



