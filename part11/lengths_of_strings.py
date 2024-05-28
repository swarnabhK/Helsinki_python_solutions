# WRITE YOUR SOLUTION HERE:
# Please write a function named lengths(strings: list) which takes a list of strings as its argument. The function should return a dictionary with the strings in the list as the keys and their lengths as the values.


def lengths(strings):
  return {s: len(s) for s in strings}


word_list = ["once", "upon" , "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)
