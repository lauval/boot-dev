class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (2 * self.length) + (2 * self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
