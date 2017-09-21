class Car:
   def move(self):
     print("car moving..")
        
class Bike:
    def move(self):
      print("bike moving..")
    
class Traveller():
    def __init__(self):
        self._car = Car()

    def start_journey(self):
        self._car.move()
    
sam = Traveller()
sam.start_journey()
