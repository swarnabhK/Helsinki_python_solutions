s_file = input("Student information: ")
e_file = input("Exercises completed: ")
names = {}
exercises = {}
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

for i,name in names.items():
  if i in exercises:
    exs = exercises[i]
    print(f"{name} {exs}")
  else:
    print(f"{name} 0")

