class Triangle():
    def __init__(self, a):
        self.side = a
    def calculate_perimeter(self):
        return self.side * 3

class Square():
    def __init__(self, a):
        self.side = a
    def calculate_perimeter(self):
        return self.side * 4

square = Square(10)
triangle = Triangle(10)

print (square.calculate_perimeter())
print (triangle.calculate_perimeter())
    


