class Squarerec:
    def __init__(self, w, length):
        self.width = w
        self.length = length

    def peri(self):
        return 2 * (self.width + self.length)

    def get_area(self):
        return self.width * self.length

    def __str__(self):
        return f"{self.length * self.width}."

    def __repr__(self):
        return f"Area of rectangle is {self.length * self.width}"


class Square(Squarerec):
    def __init__(self, side):
        super().__init__(side, side)
        self.length = self.get_area()

    def get_number_enclosing(self, new_square):
        return int(self.get_area() / new_square.get_area()) ** 2

    def __str__(self):
        return f"{self.length * self.width}."

    def __repr__(self):
        return f"Area of square is {self.length * self.width}."








