class Person:
    def __init__(self,name,height) -> None:
        self.name = name
        self.height = height

    def __str__(self) -> str:
        return f"{self.name} ({self.height} cm)"
class Room:
    def __init__(self) -> None:
        self.persons = []
    
    def add(self,person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons)==0
    
    def print_contents(self):
        print(self)
        for person in self.persons:
            print(person)
    
    def shortest(self):
        if(self.is_empty()):
            return None
        mini = self.persons[0].height
        mini_person = self.persons[0]
        for i in range(1,len(self.persons)):
            if(self.persons[i].height<mini):
                mini = self.persons[i].height
                mini_person = self.persons[i]
        return mini_person
    
    def remove_shortest(self):
        shortest = self.shortest()
        self.persons.remove(shortest)
        return shortest
    
    def __str__(self) -> str:
        combined_height = sum(person.height for person in self.persons)
        return f"There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm"
    

room = Room()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))
room.print_contents()

print()

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")

print()

room.print_contents()

