"""
Please define the class Pet. The class should include a constructor, which takes the initial values of the attributes name, species and year_of_birth as its arguments, in that specific order.

Please also write a function named new_pet(name: str, species: str, year_of_birth: int) outside the class definition. The function should create and return a new object of type Pet, as defined in the class Pet.

"""
class Pet:
    def __init__(self,name,species,year_of_birth) -> None:
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(name,species,year_of_birth):
    pet = Pet(name,species,year_of_birth)
    return pet


fluffy = new_pet("Fluffy","dog",2017)
print(fluffy.name)
print(fluffy.species)