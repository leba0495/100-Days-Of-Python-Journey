class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "pennie": 0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many coins {coin}? ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your {self.CURRENCY}{change}")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money to cover the bill.")
            self.money_received = 0
            return False
