class Hexagon:
    def __init__(self, a):
        self.side = a
    def calculate_perimeter(self):
        return self.side * 6

hexagon = Hexagon(10)
print (hexagon.calculate_perimeter())
