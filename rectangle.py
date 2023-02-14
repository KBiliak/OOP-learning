class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(4, 5)
area = rectangle.area()
print(f"area of the rectangle: {area}, where width: {rectangle.width},"
              f"height: {rectangle.height}")

perimeter = rectangle.perimeter()
print(f"perimeter of the rectangle: {perimeter}, where width: {rectangle.width},"
              f"height: {rectangle.height}")
