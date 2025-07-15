class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'sub':
            return self.a - self.b
        elif operation == 'mul':
            return self.a * self.b
        elif operation == 'div':
            return self.a / self.b if self.b != 0 else "Division by zero"
        else:
            return "Invalid operation"
calc = Calculator(10, 5)
print(calc.calculate("add"))