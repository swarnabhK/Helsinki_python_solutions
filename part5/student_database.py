def add_student(students,student):
  students[student] = {'courses':[],'total_grade':0,'avg_grade':0,'total_courses':0}

def add_course(students,student,course):
  if course[1]==0:
    return
  updated = False
  for i,c in enumerate(students[student]['courses']):
    if c[0]==course[0]:
      if course[1]>c[1]:
        students[student]['total_grade']= students[student]['total_grade']-c[1]+course[1]
        students[student]['courses'][i][1]= course[1]
        students[student]['avg_grade'] = students[student]['total_grade']/len(students[student]['courses'])
        updated = True
        break
      else:
        return
  if not updated:
    students[student]['courses'].append([course[0],course[1]])
    students[student]['total_grade']+=course[1]
    students[student]['avg_grade'] = students[student]['total_grade']/len(students[student]['courses'])
    students[student]['total_courses']+=1

def summary(students):
  print(f"students {len(students)}")
  # most courses completed
  most,name_m,ag,name_a = 0,"",0,""
  for s in students:
    if students[s]['total_courses']>most:
      most = students[s]['total_courses']
      name_m = s
    if students[s]['avg_grade']>ag:
      ag = students[s]['avg_grade']
      name_a = s
  print(f"most courses completed {most} {name_m}")
  print(f"best average grade {ag} {name_a}")

def print_student(students,student):
  grade = 0
  if student not in students:
    print(f"{student}: no such person in the database")
  else:
    courses = students[student]['courses']
    print(f"{student}:")
    if len(courses)==0:
      print(" no completed courses")
    else:
      print(f" {len(courses)} completed courses:")
      for course in courses:
        grade+= course[1]
        print(f"  {course[0]} {course[1]}")
      print(f" average grade {grade/len(courses):.1f}")

students = {}
add_student(students, "Emily")
add_student(students, "Peter")
add_course(students, "Emily", ("Software Development Methods", 4))
add_course(students, "Emily", ("Software Development Methods", 5))
add_course(students, "Peter", ("Data Structures and Algorithms", 3))
add_course(students, "Peter", ("Models of Computation", 0))
add_course(students, "Peter", ("Data Structures and Algorithms", 2))
add_course(students, "Peter", ("Introduction to Computer Science", 1))
add_course(students, "Peter", ("Software Engineering", 3))
summary(students)