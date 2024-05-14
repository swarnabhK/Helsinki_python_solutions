# Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
# Calling spruce(3) should print out


def whitespaces(n):
  for _ in range(n):
    print(" ",end="")

def stars(n):
  for _ in range(n):
    print("*",end="")


def spruce(n):
  print("a spruce!")
  for i in range(n):
    ws = (2*n-1-(2*i+1))//2
    st = 2*i+1
    whitespaces(ws)
    stars(st)
    whitespaces(ws)
    print()
  sp = (2*n-1)//2
  whitespaces(sp)
  stars(1)
  whitespaces(sp)


spruce(5)