# tee ratkaisusi tänne

from collections import defaultdict
class Course:
  def __init__(self,course,grade,credits):
    self.course = course
    self.grade = int(grade)
    self.credits = int(credits)
  
  def __str__(self):
    return f"{self.course} ({self.credits} cr) grade {self.grade}"

class Courses:
  def __init__(self):
    self.__courses = {}
  
  def add_course(self,course,grade,credits):
    if course in self.__courses:
      c = self.__courses[course]
      #check if the current grade is less than the new grade, if yes modify the object
      if grade>c.grade:
        c.grade = grade
    else:
      c = Course(course,grade,credits)
      self.__courses[course] = c
  
  def get_course_data(self,course):
    if course in self.__courses:
      print(self.__courses[course])
    else:
      print("no entry for this course")
  
  def statistics(self):
    cs = len(self.__courses)
    crs,tg = 0,0
    gd = defaultdict(int)
    for co in self.__courses:
      c = self.__courses[co]
      crs+=c.credits
      tg+=c.grade
      gd[c.grade]+=1
    try:
      avg = tg/cs
    except:
      avg=0
    print(f"{cs} completed courses, a total of {crs} credits")
    print(f"mean {avg}")
    print("grade distribution")
    for k in range(5,0,-1):
      print(f"{k}: {'x'*gd[k]}")

class CourseApplication:
  def __init__(self):
    self.__app = Courses()
  
  def execute(self):
    print("1 add course")
    print("2 get course data")
    print("3 statistics")
    print("0 exit")
    while True:
      choice = int(input("command: "))
      if choice==1:
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__app.add_course(course,grade,credits)
      elif choice==2:
        course = input("course: ")
        self.__app.get_course_data(course)
      elif choice==3:
        self.__app.statistics()
      else:
        break


e = CourseApplication()
e.execute()