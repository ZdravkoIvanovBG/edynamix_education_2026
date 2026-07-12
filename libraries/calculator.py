class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def substract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.substract(10, 20))
print(calculator.multiply(10, 20))
print(calculator.divide(10, 20))
