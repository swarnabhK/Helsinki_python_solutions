"""Please write a class named NumberStats with the following methods:

the method add_number adds a new number to the statistical record
the method count_numbers returns the count of how many numbers have been added
At this point there is no need to store the numbers themselves in any data structure. It is enough to simply remember how many have been added. The add_number method does take an argument, but there is no need to process the actual value in any way just yet.

The exercise template contains the following skeleton for the class definition:

"""

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.numbers+=1
        self.sum+=number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.sum
    def average(self):
        return self.get_sum()/self.count_numbers() if self.count_numbers()>0 else 0

# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())

# #case where no numbers have been added
# stats2 = NumberStats()
# print(stats2.get_sum())
# print(stats2.average())



#Part3 Please write a main program which keeps asking the user for integer numbers until the user types in -1. The program should then print out the sum # and the mean of the numbers typed in.

stats = NumberStats()
stats_odd = NumberStats()
stats_even = NumberStats()
print("Please type in integer numbers: (-1 to stop)")
while(True):
    number = int(input())
    if(number==-1):
        break
    stats.add_number(number)
    if(number%2==0):
        stats_even.add_number(number)
    elif(number%2==1):
        stats_odd.add_number(number)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {stats_even.get_sum()}")
print(f"Sum of odd numbers: {stats_odd.get_sum()}")