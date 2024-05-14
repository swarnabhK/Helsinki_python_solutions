# Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.


def same_char(s,i1,i2):
  if i1>len(s) or i2>len(s):
    return False
  return s[i1]==s[i2]


print(same_char("programmer", 6, 7)) # True

# different characters p and r
print(same_char("programmer", 0, 4)) # False

# the second index is not within the string
print(same_char("programmer", 0, 12)) # False