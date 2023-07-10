#!/usr/bin/python3
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(BaseGeometry):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

rectangle = Rectangle(4, 5)
print(rectangle.area())  # Output: 20

circle = Circle(3)
print(circle.area())     # Output: 28.27431

geometry = BaseGeometry()
geometry.area()          # Raises an Exception with the message "area() is not implemented"
