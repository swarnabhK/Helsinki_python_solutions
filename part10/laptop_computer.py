# Write your solution here:
# The exercise template contains a class definition for a Computer, which has the attributes model and speed.
# Please define a class named LaptopComputer which inherits the class Computer. The constructor of the new class should take a third argument: weight, of type integer.
# Please also include a __str__ method in your class definition. See the example below for the expected format of the string representation printed out.



class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def models(self):
        return self.__model

    @property
    def speeds(self):
        return self.__speed

class LaptopComputer(Computer):
    def __init__(self,model,speed,weight):
        super().__init__(model,speed)
        self.__weight = weight
    
    def __str__(self):
        return f"{self.models}, {self.speeds} MHz, {self.__weight} kg"
    

laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)

