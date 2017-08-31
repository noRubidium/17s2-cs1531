class Student(object):
    """docstring for Student."""
    def __init__(self, arg):
        super(Student, self).__init__()
        self.__id = 100
        # security -> don't want other people to modify the attributes
        # hide the actual data abd provide methods that have a clear definition of how to use/set the data
