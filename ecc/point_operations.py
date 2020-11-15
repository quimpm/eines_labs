import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_identity(self):
        return math.isinf(self.x) or math.isinf(self.y)

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

class PointAritmethics:

    @staticmethod
    def negative_of_a_point(point):
        return Point(point.x, -point.y)

    @staticmethod
    def sum_of_points(self, point1, point2, a):
        if point1.is_identity() and point2.is_identity():
           return Point(math.inf, math.inf)
        elif point1.is_identity() and not point2.is_identity():
            return Point(point2.x, point2.y)
        elif not point1.is_identity() and point2.is_identity():
            return Point(point1.x, point1.y)
        else:
            return self.calculate_new_point(point1, point2, a)

    @staticmethod
    def double_of_point(self, point, a):
        return self.sum_of_points(point, point, 0)

    @staticmethod
    def scalar_multiplication(self, point, num):
        if num == 0:
            return Point(math.inf, math.inf)
        if num % 2 == 0:
            point = self.scalar_multiplication(num / 2, point)
            return self.sum_of_points(point, point)
        return self.sum_of_points(point, self.scalar_multiplication(num - 1, point))

    #Calculate lambda and the resulting point with it
    def calculate_new_point(self, point1, point2, a):
        if point1 != point2:
            lamb = (point2.y - point1.y) / (point2.x - point1.x)
        else:
            lamb = (3*math.pow(point1.x, 2) + a) / 2*point1.y
        x = math.pow(lamb, 2) - point1.x - point2.x
        y = lamb*(point1 - x) - point1.y
        return Point(x,y)
    
    
    def binary_exponentiation(self, n1, n2):
        if n2 == 0:
            return 1
        res = self.binary_exponentiation(n1, n2 / 2)
        if (n2 % 2):
            return res * res * n1
        else:
            return res * res