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
