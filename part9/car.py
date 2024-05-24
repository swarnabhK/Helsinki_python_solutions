# WRITE YOUR SOLUTION HERE:

# Please implement a class named Car which has two private, encapsulated variables: the amount of petrol in the tank (0 to 60 litres) and odometer reading (in kilometres). The car consumes one litre of petrol per kilometre.

# The class should also contain the following methods:

# fill_up() which fills up the tank
# drive(km:int) which drives the car for the distance indicated, or for however long the petrol in the tank allows
# __str__ which returns a string representation of the car as per the examples below

class Car:
  def __init__(self):
    self.__petrol_left = 0
    self.__odometer = 0
  
  def fill_up(self):
    self.__petrol_left = 60
  
  def drive(self,km):
    if self.__petrol_left-km<0:
      self.__odometer = 60
      self.__petrol_left = 0
    else:
      self.__odometer+=km
      self.__petrol_left-=km
  
  def __str__(self):
    return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol_left} litres"


car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)
