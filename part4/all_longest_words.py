# Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.

# The order of the strings in the returned list should be the same as in the original.



def length_longest(l):
  lt = len(l[0])
  for i in range(1,len(l)):
    if len(l[i])>=lt:
      lt = len(l[i])
  return lt

def all_the_longest(l):
  lt = length_longest(l)
  result = []
  for word in l:
    if len(word)==lt:
      result.append(word)
  return result


my_list = ["first", "second", "fourth", "eleventh"]
result = all_the_longest(my_list)
print(result) # ['eleventh']
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']
