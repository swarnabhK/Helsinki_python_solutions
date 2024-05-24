# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []
        self.comb_height = 0
    def add(self,person):
        self.people.append(person)
        self.comb_height+=person.height
    def is_empty(self):
        return len(self.people)==0
    
    def print_contents(self):
        print(f"There are {len(self.people)} persons in the room, and their combined height is {self.comb_height} cm")
        for p in self.people:
            print(f"{p.name} ({p.height} cm)")
    def shortest(self):
        if self.is_empty():
            return None
        sh,short = float("inf"),""
        for p in self.people:
            if p.height<sh:
                sh = p.height
                short = p
        return short
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        sh,idx = self.shortest(),0
        for i,p in enumerate(self.people):
            if p==sh:
                self.comb_height-=p.height
                idx = i
                break
        return self.people.pop(idx)


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
