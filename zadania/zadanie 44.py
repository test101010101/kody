class Square:
    def __init__(self, a):
        self.side = a
    def change_size(self, c):
        self.change = c
        self.side = self.side + self.change
