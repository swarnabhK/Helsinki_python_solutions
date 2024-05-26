# Write your solution here:
# we have three classes, Item, suitcases and cargohold, suitcases can hold multiple items, cargo can hold multiple suitcases
# based on the max weight condition, we are using private attributes for each class, so that the client doesn't have access 
# to any of the private attributes, and cannot change the integrity of the object.

class Item:
  def __init__(self,name,weight):
    self.__name = name
    self.__weight = weight
  
  def name(self):
    return self.__name

  def weight(self):
    return self.__weight
  
  def __str__(self):
    return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
  def __init__(self,max_weight):
    self.__max_weight = max_weight
    self.__comb_weight = 0
    self.__items = []  

  def add_item(self,item):
    nw = self.__comb_weight+item.weight()
    if nw<=self.__max_weight:
      self.__items.append(item)
      self.__comb_weight+=item.weight()
  
  def __str__(self):
    it = "item" if len(self.__items)==1 else "items"
    return f"{len(self.__items)} {it} ({self.__comb_weight} kg)"

  def print_items(self):
    for p in self.__items:
      print(p)

  def weight(self):
    return self.__comb_weight
  
  def heaviest_item(self):
    heavy,h = "",0
    for it in self.__items:
      if it.weight()>h:
        h = it.weight()
        heavy = it
    return heavy


class CargoHold:

  def __init__(self,max_weight):
    self.__max_weight = max_weight
    self.__suitcases = []
    self.__comb_weight = 0
  
  def add_suitcase(self,suitcase):
    nw = self.__comb_weight+suitcase.weight()
    if nw<=self.__max_weight:
      self.__suitcases.append(suitcase)
      self.__comb_weight+=suitcase.weight()

  def __str__(self):
    #prints out the number of suitcases and the remaining space in the cargo hold, (max_weight-comb_weight)
    s = "suitcase" if len(self.__suitcases)==1 else "suitcases"
    return f"{len(self.__suitcases)} {s}, space for {self.__max_weight-self.__comb_weight} kg"
    

cargo_hold = CargoHold(1000)
print(cargo_hold)

book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold.add_suitcase(adas_suitcase)
print(cargo_hold)

cargo_hold.add_suitcase(peters_suitcase)
print(cargo_hold)
