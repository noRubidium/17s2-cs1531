class Graphic:

    def area_calculator(self, shape):
        if isinstance(shape, Rectangle):
            return shape._length * shape._width
        elif isinstance(shape, Circle):
            return 3.14 * shape._radius * shape._radius
        else: print("shape not defined")

    def scale(self, shape, ratio):
        if isinstance(shape, Rectangle):
            shape._length *= ratio
            shape._width *= ratio
        elif isinstance(shape, Circle):
            shape.radius *= ratio
        else: print("shape not defined")

class Shape(ABCMeta):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def scale(self, ratio):
        pass

class Circle(Shape):
    """docstring for Circle."""
    def __init__(self, arg):
        super(Circle, self).__init__()
        self.arg = arg

    def area(self):
        return 3.14 * self._radius ** 2

    def scale (self, ratio):
        self._radius *= ratio
