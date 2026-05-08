# 3
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def deposit(self, x):
        self._balance += x

    def withdraw(self, pin, x):
        if pin == self.__pin:
            self._balance -= x
        else:
            print("xato beradi")

    def check_balance(self):
        print(f"owner: {self.owner}, balance: {self._balance}, pin: {self.__pin}")


b1 = BankAccount(150, 70, "Wrong pin")
b1.check_balance()

b1.deposit(30)
b1.check_balance()

b1.check_balance()
