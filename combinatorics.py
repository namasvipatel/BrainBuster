# combinatorics.py

class Combinatorics:
    def factorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def permutations(self, n, r):
        return self.factorial(n) / self.factorial(n - r)

    def combinations(self, n, r):
        return self.factorial(n) / (self.factorial(r) * self.factorial(n - r))

    def pascal_triangle(self, rows):
        triangle = []
        for i in range(rows):
            row = []
            for j in range(i + 1):
                row.append(int(self.combinations(i, j)))
            triangle.append(row)
        return triangle

    def fibonacci(self, n):
        sequence = []
        a, b = 0, 1
        for _ in range(n):
            sequence.append(a)
            a, b = b, a + b
        return sequence

    def partition(self, n, m=None):
        if m is None:
            m = n
        if n == 0:
            return 1
        if n < 0 or m == 0:
            return 0
        return self.partition(n - m, m) + self.partition(n, m - 1)

    def bell_number(self, n):
        bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        bell[0][0] = 1
        for i in range(1, n + 1):
            bell[i][0] = bell[i - 1][i - 1]
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
        return bell[n][0]

    def reverse_number(self, n):
        rev = 0
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        return rev

    def octagonal_number(self, n):
        return n * (3 * n - 2)

    def sum_of_squares(self, n):
        return (n * (n + 1) * (2 * n + 1)) / 6
