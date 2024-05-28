# WRITE YOUR SOLUTION HERE:
# Please write a function named filter_forbidden(string: str, forbidden: str) which takes two strings as its arguments. The function should return a new version of the first string. It should not contain any characters from the second string.



def filter_forbidden(s,fb):
  return "".join([c for c in s if c not in fb])



sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)

