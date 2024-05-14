# Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.

# The list is printed out in the beginning and after each operation. Have a look at the example execution below:

l = []
c = 1
while(True):
  print(f"The list is now {l}")
  choice = input("ad(d), (r)emove or e(x)it: ")
  if choice=="d":
    l.append(c)
    c+=1
  elif choice=="r":
    c-=1
    l.pop()
  else:
    print("Bye!")
    break