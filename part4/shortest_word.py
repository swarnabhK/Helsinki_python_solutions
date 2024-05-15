def shortest(l):
  short, lt = l[0],len(l[0])
  for i in range(1,len(l)):
    if len(l[i])<lt:
      short = l[i]
      lt = len(l[i])
  return short


my_list = ["first", "second", "fourth", "eleventh"]
result = shortest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = shortest(my_list)
print(result)
