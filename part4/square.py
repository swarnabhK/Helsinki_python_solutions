# Please write a function named square, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

from Line import line

def print_square(n,s):
  for _ in range(n):
    line(n,s)


print_square(5, "*")
print()
print_square(3, "o")