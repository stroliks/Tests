
def is_palindrom(s):
    if s == "":
        return False

    if not isinstance(s, str):
        raise TypeError

    return s == s[::-1]


def average(lst):
    if not lst:
        raise ValueError("List is empty")
    return round(sum(lst) / len(lst),2)


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Dep must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Dep must be positive")
        if amount > self.__balance:
            raise ValueError("Insuficcient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount
