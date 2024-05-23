# Write your solution here
# Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.


import string
from random import choice

def generate_password(ln):
  letters = string.ascii_lowercase
  res = []
  for i in range(ln):
    res.append(choice(letters))
  return "".join(res)



for i in range(10):
    print(generate_password(8))
