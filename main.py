# Purpose of 'return self' from a class method in Python

class Calc():
    def __init__(self, number=0):
        self.number = number

    def add(self, value):
        self.number = self.number + value
        return self

    def subtract(self, value):
        self.number = self.number - value
        return self


calc = Calc()

calc.add(5).subtract(2).add(5)
print(calc.number)  # 👉️ 8

calc.subtract(5).add(3)
print(calc.number)  # 👉️ 6