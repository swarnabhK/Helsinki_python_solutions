class Car:
    def __init__(self) -> None:
        self.__amount_petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__amount_petrol = 60

    def drive(self,distance):
        if(distance>self.__amount_petrol):
            self.__odometer+= self.__amount_petrol
            self.__amount_petrol = 0      
        else:
            self.__amount_petrol-=distance
            self.__odometer+=distance
        
    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__amount_petrol} litres"


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