class Student(object):
    """docstring for Student."""
    def __init__(self):
        super(Student, self).__init__()
        self.__id = 100
"""
- ensures the object to be in a consistent state
- provide a clear interface of access data -> currency
- hide the implementation to ensure that change to the class won't affect other parts of the system


- Property @property -> @attr.setter
- abstractmethod -> tell other programmer that you need to implement these methods when you are implementing a childclass of this class
"""
