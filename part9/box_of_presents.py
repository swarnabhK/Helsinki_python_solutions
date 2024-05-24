# WRITE YOUR SOLUTION HERE:

class Present:
  def __init__(self,name,weight):
    self.name = name
    self.weight = weight
  
  def __str__(self):
    return f"{self.name} ({self.weight} kg)"

class Box:
  def __init__(self):
    self.presents = []
    self.tot_weight = 0
  
  def add_present(self,present):
    self.tot_weight+=present.weight
    self.presents.append(present)

  def total_weight(self):
    return self.tot_weight


book = Present("ABC Book", 2)

box = Box()
box.add_present(book)
print(box.total_weight())

cd = Present("Pink Floyd: Dark Side of the Moon", 1)
box.add_present(cd)
print(box.total_weight())

