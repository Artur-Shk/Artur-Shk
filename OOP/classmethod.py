class Vector:
    min_coord = 0
    max_coord = 100

    @classmethod
    def validate(cls, arg):
        return cls.min_coord <= arg <= cls.max_coord

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod

    def norm2(x, y):
        


v = Vector(1, 100)
res = Vector.get_coord(v)
print(res)
print(Vector.validate(10))
