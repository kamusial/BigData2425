"Program OOP do analizy danych sprzedażowych"

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(ID: {self.product_id}, Name: {self.name}, Price: {self.price})"


class SalesData:    # zarządzanie danymi sprzedaży
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
        info = {}
        for sale in self.sales_data.get_all_sales():
            product = sale['product']
            quantity = sale['quantity']
            if product.name not in info:
                info[product.name] = 0
            info[product.name] += quantity
        best_product = max(info, key=info.get)
        return  best_product, info[best_product]


    # def sales_summary(self):
    #     # podsumowanie sprzedaży



product1 = Product(1, 'Laptop', 3000)
product2 = Product(2, 'Phone', 1500)
product3 = Product(3, 'Headphones', 300)

sales_data = SalesData()
sales_data.add_sale(product1, 5)
sales_data.add_sale(product2, 10)
sales_data.add_sale(product3, 15)
sales_data.add_sale(product2, 5)

analysis = SalesAnalysis(sales_data)
print(f'Całkowity przychód: {analysis.revenue()} PLN')
