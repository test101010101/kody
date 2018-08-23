class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print ("Jestem figurą")



class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 50)
a_square = Square(20)

a_rectangle.what_am_i()
a_square.what_am_i()
