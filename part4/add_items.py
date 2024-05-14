# Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

l = []
no_items = int(input("Number of items to add? "))
for i in range(1,no_items+1):
  item = int(input(f"Item {i}: "))
  l.append(item)
print(l)
