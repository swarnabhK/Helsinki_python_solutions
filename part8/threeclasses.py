# Write your solution here
# Please write the three classes specified below. Each class should have exactly the same names and types of attributes as listed.
# Please also include a constructor in each class. The constructor should take the initial values of the attributes as its arguments, in the order listed below.


class Checklist():
  def __init__(self,header,entries):
    self.header = header
    self.entries = entries


class Customer():
  def __init__(self,id,balance,discount):
    self.id = id
    self.balance = balance
    self.discount = discount

class Cable():
  def __init__(self,model,length,max_speed,bidirectional):
    self.model = model
    self.length = length
    self.max_speed = max_speed
    self.bidirectional = bidirectional


