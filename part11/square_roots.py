# WRITE YOUR SOLUTION HERE:
# Please write a function named square_roots(numbers: list) which takes a list of integers as its argument. The function should return a new list containing the square roots of the original integers.



from math import sqrt

def square_roots(numbers):
  return [sqrt(num) for num in numbers]



lines = square_roots([1,2,3,4])
for line in lines:
    print(line)
