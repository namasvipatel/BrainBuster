# scalar.py

class scalar:
    def add(self, value, num):
        return value + num

    def subtract(self, value, num):
        return value - num

    def multiply(self, value, num):
        return value * num

    def divide(self, value, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        return value / num

    def power(self, value, exponent):
        return value ** exponent

    def modulus(self, value, num):
        return value % num

    def negate(self, value):
        return -value

    def absolute(self, value):
        return abs(value)

    def is_positive(self, value):
        return value > 0

    def is_zero(self, value):
        return value == 0
