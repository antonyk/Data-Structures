"""
1. design a 2d vector class

"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"2D Vector: (X: {self.x}, Y: {self.y})"

    def __add__(self, other):
        ret = Vector(self.x, self.y)
        ret.x += other.x
        ret.y += other.y
        return ret

    def __sub__(self, other):
        ret = Vector(self.x, self.y)
        ret.x -= other.x
        ret.y -= other.y
        return ret

    def add(self, vec):
        return self + vec

    def sub(self, vec):
        return self - vec

    def mul(self, vec):
        self.x *= vec.x
        self.y *= vec.y

    def div(self, vec):
        self.x /= vec.x
        self.y /= vec.y

    def idiv(self, vec):
        self.x //= vec.x
        self.y //= vec.y


v1 = Vector(20, 10)
v2 = Vector(10, 10)
v3 = Vector(0, 0)
print(v1, v2, v3)
v3 = v1.add(v2)
print(v1, v2, v3)

v3 = v1 + v2
print(v3)


class Test():
    pass


print(dir(Test))
