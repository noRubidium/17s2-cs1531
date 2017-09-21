from abc import abstractmethod

class Vehicle(object):
    """
    @param: db contains database connection details
    """
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):

    def move(self):
        print("moving car")

class Bike(Vehicle):

    def move(self):
        print("moving bike")

class Traveller():

    """
    Injecting the vehicle type through the method
    """
    def start_journey(self, vehicle):
        vehicle.move()

traveller_1 = Traveller()
traveller_1.start_journey(Car())

traveller_2 = Traveller()
traveller_2.start_journey(Bike())


