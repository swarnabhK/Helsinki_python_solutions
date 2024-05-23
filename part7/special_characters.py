# Write your solution here

import string
def separate_characters(str):
  letters,punc,other="","",""
  

  for c in str:
    if c in string.ascii_letters:
      letters+=c
    elif c in string.punctuation:
      punc+=c
    else:
      other+=c
  return letters,punc,other



parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])
