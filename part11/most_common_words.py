# WRITE YOUR SOLUTION HERE:
# Please write a function named most_common_words(filename: str, lower_limit: int) which takes a filename and an integer value for a lower limit as its arguments. The function should return a dictionary containing the occurrences of the words which appear at least the number of times specified in the lower_limit parameter.



# WRITE YOUR SOLUTION HERE:
import string
from collections import defaultdict
def most_common_words(filename: str, lower_limit: int):
  mc = defaultdict(int)
  with open(filename,"r") as file:
    for line in file:
      line= line.strip()
      line = "".join(c for c in line if c not in string.punctuation).split()
      for l in line:
        mc[l]+=1
  return {key:value for key,value in mc.items() if value>=lower_limit}


print(most_common_words("comprehensions.txt", 3))