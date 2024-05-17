# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.
# An example of its use:

def invert(dic):
  dic_new = {}
  for key in dic:
    value = dic[key]
    dic_new[value] = key
  dic.clear()
  dic.update(dic_new)
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)
