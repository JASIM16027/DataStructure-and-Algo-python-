from shape import polygon


class Triangle(polygon):
    def area(self):
        return (self.get_height() * self.get_width())/2
