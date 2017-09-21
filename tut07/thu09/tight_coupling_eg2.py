class Vehicle(metaclass=ABCMeta):
    @asbtractmethod
    def move(self):
        pass
class Car(Vehicle):
   def move(self):
     print("car moving..")

class Bike(Vehicle):
    def move(self):
      print("bike moving..")

class Traveller():
    def __init__(self, vehicle):
        self.__vehicle = vehicle

    def start_journey(self):
        self.__vehicle.move()

vehicle = Car()
sam = Traveller(vehicle)
sam.start_journey()
