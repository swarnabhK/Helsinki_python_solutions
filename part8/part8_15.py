class LunchCard:
    def __init__(self,balance):
        self.balance = balance
    def __str__(self):
        return f"The balance is {round(float(self.balance),1)} euros"
    def eat_lunch(self):
        bal = self.balance
        self.balance-=2.60
        if(self.balance<0):
            self.balance = bal
    def eat_special(self):
        bal = self.balance
        self.balance-=4.60
        if(self.balance<0):
            self.balance = bal
    
    def deposit_money(self,amount):
        if(amount<0):
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance+=amount

#Tests
peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f"peter: {peters_card}")
print(f"grace: {graces_card}")
peters_card.deposit_money(20)
graces_card.eat_special()
print(f"peter: {peters_card}")
print(f"grace: {graces_card}")
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"peter: {peters_card}")
print(f"grace: {graces_card}")