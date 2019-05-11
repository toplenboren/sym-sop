import math


class Vector:
    X = 0
    Y = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def print(self):
        print(self.X, self.Y)

    def __add__(self, other):
        return Vector(self.X + other.X,
                      self.Y + other.Y)

    def __mul__(self, other):
        return self.X * other.X + \
               self.Y * other.Y

    def get_len(self):
        return math.sqrt(self * self)

    def get_angle(self, other):

        if self.get_len() == 0 or other.get_len() == 0:
            raise Exception("Bad input!")

        s_mul = self * other
        cos = s_mul / (self.get_len()
                       * other.get_len())
        return math.degrees(math.acos(cos))

a = Vector(1,0)
b = Vector(0,-1)
c = a + b
d = a * b
e = a.get_angle(b)

a.print()
b.print()
c.print()
print(d)
print(e)
