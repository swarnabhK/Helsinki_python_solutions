# Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.
# You can assume the string will contain only characters from the lowercase English alphabet a...z.
# An example of expected behaviour:


# O(N), instead of using a list, we are using a set to reduce search complexity to O(N) 
def no_vowels(s):
  res = ""
  char_set = {"a","e","i","o","u"}
  for c in s:
    if c not in char_set:
      res+=c
  return res

my_string = "this is an example"
print(no_vowels(my_string))


