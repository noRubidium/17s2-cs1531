class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
   def move(self):
     print("car moving..")

class Bike(Vehicle):
    def move(self):
      print("bike moving..")

class Traveller():
    def __init__(self, v):
        self._vehicle = v

    def start_journey(self):
        self._vehicle.move()

vehicle = Car()
sam = Traveller(vehicle)
sam.start_journey()
