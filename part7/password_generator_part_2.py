# Write your solution here

import string
from random import choice,shuffle

def generate_strong_password(ln,p1,p2):
  letters = string.ascii_lowercase
  numbers = string.digits
  others = "!?=+-()#"
  res = []
  if p1==True and p2==True:
    div = ln//3
    rem = ln-(div*3)
    lt,no,ot = div+rem,div,div
    for _ in range(lt):
      res.append(choice(letters))
    for _ in range(no):
      res.append(choice(numbers))
    for _ in range(ot):
      res.append(choice(others))
  elif p1==True:
    div = ln//2
    rem = ln-(div*2)
    lt,no = div+rem,div
    for _ in range(lt):
      res.append(choice(letters))
    for _ in range(no):
      res.append(choice(numbers))
  elif p2 == True:
    div = ln//2
    rem = ln-(div*2)
    lt,ot = div+rem,div
    for _ in range(lt):
      res.append(choice(letters))
    for _ in range(ot):
      res.append(choice(others))
  else:
    lt = ln
    for _ in range(lt):
      res.append(choice(letters))
  shuffle(res)
  return "".join(res)

for i in range(10):
    print(generate_strong_password(8, False, True))
