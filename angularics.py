# angularics.py
class Angularics:

    def degrees_to_radians(self, degrees):
        return degrees * (3.141592653589793 / 180)

    def radians_to_degrees(self, radians):
        return radians * (180 / 3.141592653589793)

    def sin_deg(self, degrees):
        radians = self.degrees_to_radians(degrees)
        return self.sin(radians)

    def cos_deg(self, degrees):
        radians = self.degrees_to_radians(degrees)
        return self.cos(radians)

    def tan_deg(self, degrees):
        radians = self.degrees_to_radians(degrees)
        return self.tan(radians)

    def sin(self, radians):
        x = radians
        return x - (x**3)/6 + (x**5)/120 - (x**7)/5040  # Taylor approx

    def cos(self, radians):
        x = radians
        return 1 - (x**2)/2 + (x**4)/24 - (x**6)/720  # Taylor approx

    def tan(self, radians):
        return self.sin(radians) / self.cos(radians)

    def cot(self, radians):
        return 1 / self.tan(radians)

    def angle_between_vectors(self, x1, y1, x2, y2):
        dot_product = x1*x2 + y1*y2
        magnitude1 = (x1**2 + y1**2)**0.5
        magnitude2 = (x2**2 + y2**2)**0.5
        cos_theta = dot_product / (magnitude1 * magnitude2)
        return self.radians_to_degrees(self.acos_approx(cos_theta))

    def acos_approx(self, x):
        # Approximate acos using Taylor series for small x
        return (3.141592653589793 / 2) - (x + (x**3)/6 + (3*(x**5))/40)
