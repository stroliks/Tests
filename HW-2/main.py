class Array:

    def __init__(self, *args):
        self.array = args

    def sum(self) -> float:
        if len(self.array) ==0:
            raise ValueError
        summa = 0

        for i in self.array:
            summa += i

        return summa

    def multiply(self) -> float:
        if len(self.array) ==0:
            raise ValueError
        multiply = 1

        for i in self.array:
            multiply *= i

        return multiply

    def average(self) -> float:
        if len(self.array) ==0:
            raise ValueError
        return self.sum() / len(self.array)
