class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    def __add__(self, other):
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        raise ValueError('Vector can be summed only with other vector')


    def __sub__(self, other):
        if type(other) == Vector:
            return Vector(self.x - other.x, self.y - other.y)
        raise ValueError('Vector can be subtracted only from other vector')


    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vector(self.x * other, self.y * other)
        raise ValueError('Vector can be multiplied only on a float or int')


    def __str__(self):
        return f'({self.x}, {self.y})'


vector1 = Vector(3, 4)
vector2 = Vector(1, 2)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * 2)
