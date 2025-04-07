# calculus_beyond/calculus.py

class calculus:
    def derivative_power_rule(self, coefficient, power):
        return coefficient * power, power - 1

    def integral_power_rule(self, coefficient, power):
        new_power = power + 1
        return coefficient / new_power, new_power

    def limit_at_point(self, func, point, h=1e-5):
        return (func(point + h) - func(point)) / h

    def definite_integral_rectangle(self, func, a, b, n=1000):
        width = (b - a) / n
        total = 0
        for i in range(n):
            total += func(a + i * width) * width
        return total

    def slope_of_tangent(self, func, x, h=1e-5):
        return (func(x + h) - func(x - h)) / (2 * h)

    def area_under_curve(self, func, a, b, n=1000):
        width = (b - a) / n
        total_area = 0
        for i in range(n):
            height = (func(a + i * width) + func(a + (i + 1) * width)) / 2
            total_area += height * width
        return total_area

    def riemann_sum_left(self, func, a, b, n=1000):
        width = (b - a) / n
        total = 0
        for i in range(n):
            total += func(a + i * width) * width
        return total

    def riemann_sum_right(self, func, a, b, n=1000):
        width = (b - a) / n
        total = 0
        for i in range(1, n + 1):
            total += func(a + i * width) * width
        return total

    def riemann_sum_midpoint(self, func, a, b, n=1000):
        width = (b - a) / n
        total = 0
        for i in range(n):
            mid = a + (i + 0.5) * width
            total += func(mid) * width
        return total

    def second_derivative(self, func, x, h=1e-5):
        return (func(x + h) - 2 * func(x) + func(x - h)) / (h ** 2)
