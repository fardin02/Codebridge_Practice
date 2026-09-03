class card:
    def __init__(self,balance):
        self.balance = balance

# card = card(5000)
# card.balance = 99999999

class Card:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Denied: insufficient funds.")
            return False
        self.__balance -= amount
        print(f"Dispensed ¥{amount}. Remaining: ¥{self.__balance}")
        return True

    def check_balance(self):
        return self.__balance

def main():
    card = Card(5000)
    print(f"Welcome. Your balance is ¥{card.check_balance()}.")

    while True:
        amount = int(input("Enter amount to withdraw (0 to exit): "))
        if amount == 0:
            print(f"Goodbye. Final balance: ¥{card.check_balance()}")
            break
        card.withdraw(amount)


if __name__ == "__main__":
    main()