# In this exercise you will write a program for printing out grade statistics for a university course.
# The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.
# Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.
# The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.
# When the user types in an empty line, the program prints out statistics. They are formulated as follows:
# The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.

from collections import defaultdict 
def user_input():
  grades = []
  while(True):
    try:
      choice = input("Exam points and exercises completed: ")
      if choice=="":
        break
      exam_points,exercises_completed = map(int,choice.split(" "))
      grades.append((exam_points,exercises_completed))
    except ValueError:
      print("Invalid input. Please enter integers separated by a space.")
  return grades

def get_grade(exp,exc):
  tp = (exc//10)+exp
  if exp<10:
    return tp,0
  grade = 0
  if(tp>=0 and tp<=14):
    grade = 0
  elif(tp>=15 and tp<=17):
    grade = 1
  elif(tp>=18 and tp<=20):
    grade = 2
  elif(tp>=21 and tp<=23):
    grade = 3
  elif(tp>=24 and tp<=27):
    grade = 4
  elif(tp>=28 and tp<=30):
    grade = 5
  return tp,grade

def get_stats(l):
  points = 0
  no_failed = 0
  grade_dist = defaultdict(int)
  no_students = len(l)
  g = 5
  for exp,exc in l:
    tp,grade = get_grade(exp,exc)
    points+=tp
    if grade==0:
      no_failed+=1
    grade_dist[grade]+=1
  print("Statistics:")
  print(f"Points average: {(points/no_students):.1f}")
  print(f"Pass percentage: {((no_students-no_failed)/no_students)*100:.1f}")
  print("Grade distribution: ")
  while(g>=0):
    print(f"{g}: {grade_dist[g]*'*'}")
    g-=1

def main():
  grades = user_input()
  get_stats(grades)

main()