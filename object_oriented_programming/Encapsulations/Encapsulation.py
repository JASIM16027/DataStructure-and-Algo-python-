class Shape:
    def __init__(self, radius, height, width):
        self.__radius = radius
        self.__height = height
        self.__width = width

    def set_height(self, value):
        self.__height = value

    def get_height(self):
        return self.__height

    def set_width(self, value):
        self.__width = value

    def get_width(self):
        return self.__width

    def set_radius(self, value):
        self.__radius = value

    def get_radius(self):
        return self.__radius

    def rectangle_area(self):
        return self.__height * self.__width

    def circle_area(self):
        return 3.1617 * self.__radius * self.__radius


c = Shape(12, 6, 2)

print(c.circle_area())
c.set_height(10)
print(c.rectangle_area())

print(c.rectangle_area())