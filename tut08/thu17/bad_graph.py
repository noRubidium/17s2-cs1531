class Graphic:

    def area_calculator(self, shape):
        return shape.get_area()

    def scale(self, shape, ratio):
        shape.scale(ratio)

class Shape(metaclass=ABCMeta):
    def __init__(self):
        self.__scale = 1

    @abstractmethod
    def get_area(self):
        pass

    def scale(self, ratio):
        self.__scale *= ratio

class Circle(Shape):
    def get_area(self):
        return 3.14 * self._radius * self.radius * (self.__scale ** 2)
