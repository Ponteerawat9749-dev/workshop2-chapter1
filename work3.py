class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def show_details(self):
        print(self.product_name)
        print(self.price)

product1 = Product("E-Book", 199)
product2 = Product("Online Course", 1490)

product1.show_details()
product2.show_details()
