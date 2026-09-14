from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self, radious):
        self.radious = radious
        area = 3.14 * (self.radious)**2
        print(area)

    def calculate_perimeter(self,radious):
        self.radious = radious
        Perimeter = 2 * 3.14 * self.radious
        print(Perimeter)


class Square(Shape):
    def calculate_area(self, square):
        self.square = square
        area = (self.square)**2
        print(area)

    def calculate_perimeter(self,square):
        self.square = square
        Perimeter = 4 * self.square
        print(Perimeter)

class Rectangle(Shape):
    def calculate_area(self, width, height):
        self.width = width
        self.height = height
        area = self.width * self.height
        print(area)

    def calculate_perimeter(self,width, height):
        self.width = width
        self.height = height
        Perimeter = 2 * (self.width + self.height)
        print(Perimeter)




my_circle = Circle()
my_circle.calculate_perimeter(5)

my_rectangle = Rectangle()
my_rectangle.calculate_area(5,3)
        
my_square = Square()
my_square.calculate_area(5)


