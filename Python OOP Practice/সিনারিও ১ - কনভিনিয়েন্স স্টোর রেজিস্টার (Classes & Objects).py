class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def scan(self):
        print(f"Scanned: {self.name} - ¥{self.price}")
        return self.price

class Register:
    def __init__(self):
        self.total = 0

    def checkout(self,products):
        for p in products:
            self.total += p.scan()
        print(f"TOTAL: ¥{self.total}")

def main():
    count = int(input("How Many products? "))
    cart = []

    for _ in range(count):
        name = input("Product name: ")
        price = int(input("Price: "))
        cart.append(Product(name, price))

    register = Register()
    register.checkout(cart)

if __name__ == "__main__":
    main()