# wwite your solution here
def find_grade(pts):
  if 0<=pts<=14:
    return 0
  elif 15<=pts<=17:
    return 1
  elif 18<=pts<=20:
    return 2
  elif 21<=pts<=23:
    return 3
  elif 24<=pts<=27:
    return 4
  elif pts>=28:
    return 5

s_file = input("Student information: ")
e_file = input("Exercises completed: ")
ep_file = input("Exam points: ")
names = {}
exercises = {}
exam_points = {}
with open(s_file) as sfile:
  for line in sfile:
    line = line.split(";")
    if line[0]=='id':
      continue
    names[line[0]] = line[1]+" "+line[2].strip()
with open(e_file) as efile:
  for line in efile:
    line = line.split(";")
    if line[0]=='id':
      continue
    exercises[line[0]] = sum(list(map(int,line[1:])))

with open(ep_file) as epfile:
  for line in epfile:
    line = line.split(";")
    if line[0]=='id':
      continue
    exam_points[line[0]] = sum(list(map(int,line[1:])))  
for i,name in names.items():
  exs,pts = 0,0
  if i in exercises:
    exs = exercises[i]
    ex_points = int((exs/40)*10)
  if i in exam_points:
    pts = exam_points[i]
  total_points = ex_points+pts
  grade = find_grade(total_points)  
  print(f"{name} {grade}")
