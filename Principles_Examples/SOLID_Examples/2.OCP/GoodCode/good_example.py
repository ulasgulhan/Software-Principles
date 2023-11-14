class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area

rectangle = Rectangle(5, 10)
circle = Circle(7)

calculator = AreaCalculator()
total_area = calculator.calculate_area([rectangle, circle])

print(f"Toplam alan: {total_area}")