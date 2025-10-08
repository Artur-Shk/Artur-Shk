from accessify import private, protected

class Vector:
    min_coord = 0
    max_coord = 100

    @private
    @classmethod
    def validate(cls, arg):
        return cls.min_coord <= arg <= cls.max_coord

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(1, 2)
print(Vector.norm2(5, 6))
res = Vector.get_coord(v)
print(res)