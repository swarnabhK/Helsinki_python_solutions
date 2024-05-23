# Write your solution here

import os
def filter_incorrect():
  if os.path.exists("correct_numbers.csv"):
    with open("correct_numbers.csv","w") as f:
      pass
  with open("lottery_numbers.csv","r") as file:
    with open("correct_numbers.csv","a") as wfile:
      for line in file:
        line = line.strip()
        if verify_line(line):
          wfile.write(line+"\n")



def verify_line(line):

  # One or more numbers are not correct: week 22;1,**,5,6,13,2b,34

  # Too few numbers: week 13;4,6,17,19,24,33 shoulld be 7

  # The numbers are too small or large: week 39;5,9,15,35,39,41,105 (between 1 and 39)

  # the same number appears twice: week 41;5,12,3,35,12,14,36.
  line_sp = line.split(";")
  try:
    week = line_sp[0].split(" ")
    week_no = int(week[1])
  except:
    print("Week no is not a number")
    return False
  try:
    numbers = line_sp[1].split(',')
    numbers = list(map(int,numbers))
  except:
    print("One of the numbers is not numeric")
    return False

  if len(numbers)!=7 or len(set(numbers))!=7:
    print("7 numbers not present or same number present more than once")
    return False
  for n in numbers:
    if n<1 or n>39:
      print("Number doesn't fall in the range")
      return False
  print("Okay, returing true")
  return True
    


filter_incorrect()