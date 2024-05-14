# Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:

# in the order the items were added
# ordered from smallest to greatest
# The program exits when the user types in 0.


l = []

while(True):
  value = int(input("New item: "))
  if value==0:
    print("Bye!")
    break
  l.append(value)
  print(f"The list now: {l}")
  print(f"The list in order:{sorted(l)}")