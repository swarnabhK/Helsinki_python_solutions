# Please create a class named BankAccount which models a bank account. The class should contain

# a constructor which takes the name of the owner (str), account number (str) and balance (float) as arguments
# a method deposit(amount: float) for depositing money to the account
# a method withdraw(amount: float) for withdrawing money from the account
# a getter method balance which returns the balance of the account
# The class should also contain the private method

# __service_charge(), which decreases the balance on the account by one percent. Whenever either of the methods deposit or withdraw is called, this method should also be called. The service charge is calculated and subtracted only after the actual operation is completed (that is, after the amount specified has been added to or subtracted from the balance).
# All data attributes within the class definition should be private.

class BankAccount:
  def __init__(self,owner,account_no,balance):
    self.__owner = owner
    self.__account_no = account_no
    self.__balance = balance
  
  def deposit(self,amount):
    self.__balance+=amount
    self.__service_charge()
  
  def withdraw(self,amount):
    self.__balance-=amount
    self.__service_charge()
  
  def balance(self):
    return self.__balance
  
  def __service_charge(self):  
    self.__balance -=(0.01*self.__balance)

  @property
  def balance(self):
    return self.__balance
  



account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)
