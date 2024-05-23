# Write your solution here
# Please write a function named lottery_numbers(amount: int, lower: int, upper: int), which generates as many random numbers as specified by the first argument. All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned. The numbers should be in ascending order in the returned list.

# As these are lottery numbers, no number should appear twice in the list.


from random import sample

def lottery_numbers(amount,lower,upper):
  l  = list(range(lower,upper+1))
  lo = sample(l,amount)
  return lo



for number in lottery_numbers(7, 1, 40):
    print(number)
