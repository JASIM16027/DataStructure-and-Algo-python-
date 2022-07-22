from rectangle import Rectangle
from triangle import Triangle

rectangle = Rectangle()
rectangle.set_method(100, 10)
triangle = Triangle()
triangle.set_method(20, 10)
print(rectangle.area())
print(triangle.area())
rectangle.set_method(100, 1011)
print(rectangle.area())