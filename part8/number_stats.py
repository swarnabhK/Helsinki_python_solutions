# Write your solution here!
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
        try:
            return self.get_sum()/self.count_numbers()
        except:
            return 0


stats = NumberStats()
even = NumberStats()
odd = NumberStats()

print("Please type in integer numbers: ")
while True:
    no = int(input())
    if no==-1:
        break
    stats.add_number(no)
    if no%2==0:
        even.add_number(no)
    else:
        odd.add_number(no)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odd.get_sum()}")

