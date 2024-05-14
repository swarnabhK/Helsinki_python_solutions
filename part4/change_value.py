# Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.


l = [1, 2, 3, 4, 5]
print(l)
while(True):
  idx = int(input("Enter an index(0-4), -1 to exit: "))
  if idx==-1:
    break
  value = int(input("Enter the value to replace at index: "))
  l[idx] = value
  print(l)