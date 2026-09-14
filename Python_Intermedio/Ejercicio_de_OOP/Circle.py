class Circle:
    def __init__(self, radius):
        self.radius = radius


    def get_area(self):
        self.area = 3.14 * (self.radius**2)
        print(f"area: {self.area}")

circle1 = Circle(5)
circle1.get_area()