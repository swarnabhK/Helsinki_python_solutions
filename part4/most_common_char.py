# Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

#Brute force using count method

def most_common_character(s):
  max_count = 0
  char = ""
  for c in s:
    curr_count = s.count(c)
    if(curr_count>max_count):
      char = c
      max_count = curr_count
  return char

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))
