# Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.
# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

from Line import line

def shape(n1,f1,n2,f2):
  #print the triangle first with n1 as the height and f1 as the triangle character
  for i in range(1,n1+1):
    line(i,f1)
  #print the rectangle with n1 as the width, n2 as the height and f2 as the filler character
  for i in range(n2):
    line(n1,f2)


shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")

