# Write your solution here
import os

def filter_solutions():
  if os.path.exists("correct.csv"):
    with open("correct.csv","w") as f:
      pass
  if os.path.exists("incorrect.csv"):
    with open("incorrect.csv","w") as f:
      pass
  with open("solutions.csv","r") as file:
    for line in file:
      line = line.strip()
      a = line.split(";")
      for c in a[1]:
        if c=='-' or c=='+':
          ch = a[1].split(c)
          break
      op1,fn,op2 = ch[0],c,ch[1]
      if fn=='+':
        val = int(op1)+int(op2)
      elif fn=='-':
        val = int(op1)-int(op2)
      if val==int(a[2]):
        with open("correct.csv","a") as corr:
          corr.write(line+"\n")
      elif val!=int(a[2]):
        with open("incorrect.csv","a") as inc:
          inc.write(line+"\n")
    

# no matter how many times the function is called, the file should be overwritten and new results should be pushed
filter_solutions()
filter_solutions()