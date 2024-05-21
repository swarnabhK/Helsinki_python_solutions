def collatz(no):
  val = 0
  if no%2==0:
    val = no//2
    print(val)
  else:
    val = (3*no)+1
    print(val)
  return val


try:
  choice = int(input("Enter number: "))
  c = choice
  while True:
    v = collatz(c)
    if v==1:
      break
    c = v
except ValueError:
  print("You must input an integer!")


  