# Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.

from Line import line

def box_of_hash(n):
  for _ in range(n):
    line(10,"#")


box_of_hash(5)
print()
box_of_hash(2)
