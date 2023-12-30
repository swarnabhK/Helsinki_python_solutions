"""
Please write the three classes specified below. Each class should have exactly the same names and types of attributes as listed.
Please also include a constructor in each class. The constructor should take the initial values of the attributes as its arguments, in the order listed below.
1.Class Checklist
attribute header (string)
attribute entries (list)
2.Class Customer
attribute id (string)
attribute balance (float)
attribute discount (integer)
3.Class Cable
attribute model (string)
attribute length (float)
attribute max_speed (integer)
attribute bidirectional (Boolean)
"""


class Checklist:
    def __init__(self,header,entries) -> None:
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self,id,balance,discount) -> None:
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self,model,length,max_speed,bidirectional) -> None:
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


checklist = Checklist("To do",['wake up','do laundry','clean house','study'])
customer = Customer("1234",234.45,30)
cable = Cable("DishTv",100.25,40,True)


print(f"The checklist attributes are 1){checklist.header} and 2){checklist.entries}")
print(f"The customer attributes are 1){customer.id}, 2){customer.balance} and 3){customer.discount}")
print(f"The checklist attributes are 1){cable.model}, 2){cable.length}, 3){cable.max_speed} and 4){cable.bidirectional}")