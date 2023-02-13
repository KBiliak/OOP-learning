import math
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def calc_circumference(self):
        circumference = 2 * math.pi * self.radius
        print(f"circumference of the circle: {circumference}, color: {self.color}")
        return circumference

    def calc_area(self):
        area = math.pi * self.radius * self.radius
        print(f"area of the circle:{area}, color: {self.color}")

calc_Circle = Circle(4, "GREEN")
calc_Circle.calc_circumference()
calc_Circle.calc_area()
