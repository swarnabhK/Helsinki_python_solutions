# write your solution here

def largest():
  large = -float("inf")
  with open("numbers.txt") as new_file:
    for line in new_file:
      line = int(line.replace("\n",""))
      if line>large:
        large = line
  return large