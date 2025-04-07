# datanox_operations.py
class datanox:
    
    def mean(self, data):
        return sum(data) / len(data)

    def median(self, data):
        data = sorted(data)
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]

    def mode(self, data):
        freq = {}
        for num in data:
            freq[num] = freq.get(num, 0) + 1
        max_count = max(freq.values())
        for num, count in freq.items():
            if count == max_count:
                return num

    def variance(self, data):
        mean_val = self.mean(data)
        return sum((x - mean_val) ** 2 for x in data) / len(data)

    def std_deviation(self, data):
        return self.variance(data) ** 0.5

    def min_value(self, data):
        return min(data)

    def max_value(self, data):
        return max(data)

    def range_value(self, data):
        return max(data) - min(data)

    def sum_values(self, data):
        return sum(data)

    def normalize(self, data):
        min_val = min(data)
        max_val = max(data)
        if max_val == min_val:
            return data
        return [(x - min_val) / (max_val - min_val) for x in data]
