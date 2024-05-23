# Write your solution here
# Please write a function named smallest_average(person1: dict, person2: dict, person3: dict), which takes three dictionary objects as its arguments.

# Each dictionary object contains values mapped to the following keys:

# "name": The name of the contestant
# "result1": the first result of the contestant (an integer between 1 and 10)
# "result2": the second result of the contestant (as above)
# "result3": the third result of the contestant (as above)
# The function should calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest. The return value should be the entire dictionary object containing the contestant's information.



def calc_avg(p):
  tot = 0
  for k in p:
    if k=='name':
      continue
    tot+=p[k]
  return tot/3
def smallest_average(p1,p2,p3):
  person = [p1,p2,p3]
  small,dic = float("inf"), {}
  for p in person:
    c = calc_avg(p)
    if c<small:
      small = c
      dic = p
  return dic


person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))

