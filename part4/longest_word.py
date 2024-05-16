def length_of_longest(l):
  longest,long_length = l[0], len(l[0])
  for i in range(1,len(l)):
    if len(l[i])>long_length:
      longest = l[i]
      long_length = len(l[i])
  return longest, long_length


my_list = ["first", "second", "fourth", "eleventh"]

str, length = length_of_longest(my_list)
print(f"Longest string is: {str} and the length is: {length}")
  