# wwite your solution here
def add_student(id):
  student_data[id] = {'name':'','exec_nbr':0,'exec_pts':0,'exm_pts':0,'tot_pts':0,'grade':0}

def print_students(st):
  name,exec_nbr,exec_pts,exm_pts,tot_pts,grade = 'name','exec_nbr','exec_pts.','exm_pts.','tot_pts.','grade'
  print(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade:10}")
  for p in st:
    s = st[p]
    print(f"{s['name']:30}{s['exec_nbr']:<10}{s['exec_pts']:<10}{s['exm_pts']:<10}{s['tot_pts']:<10}{s['grade']:<10}")

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
student_data = {}

with open(s_file) as sfile:
  for line in sfile:
    line = line.split(";")
    if line[0]=='id':
      continue
    add_student(line[0])
    n = line[1]+" "+line[2].strip()
    names[line[0]] = n
    student_data[line[0]]['name'] = n
with open(e_file) as efile:
  for line in efile:
    line = line.split(";")
    if line[0]=='id':
      continue
    e = sum(list(map(int,line[1:])))
    exercises[line[0]] = e
    student_data[line[0]]['exec_nbr'] = e

with open(ep_file) as epfile:
  for line in epfile:
    line = line.split(";")
    if line[0]=='id':
      continue
    ep = sum(list(map(int,line[1:])))
    exam_points[line[0]] =  ep
    student_data[line[0]]['exm_pts'] = ep 
for i,name in names.items():
  exs,pts = 0,0
  if i in exercises:
    exs = exercises[i]
    ex_points = int((exs/40)*10)
    student_data[i]['exec_pts'] = ex_points
  if i in exam_points:
    pts = exam_points[i]
  total_points = ex_points+pts
  student_data[i]['tot_pts'] = total_points
  grade = find_grade(total_points)  
  student_data[i]['grade'] = grade

print_students(student_data)