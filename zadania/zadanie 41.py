class Triangle:
    def __init__(self, a, h):
        self.side = a
        self.height = h
    def area(self):
        return self.side * self.height


triangle = Triangle(10, 5)
print (triangle.area())
