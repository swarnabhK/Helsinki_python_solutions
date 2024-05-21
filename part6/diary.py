# Write your solution here
# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. 
# When the program is executed, it should first read any entries already in the file.


while(True):
  print("1 - add an entry, 2- read entries, 0 - quit")
  choice = int(input("Function: "))
  if choice==0:
    print("Bye now!")
    break
  elif choice==1:
    line = input("Diary entry: ")
    with open("diary.txt","a") as write_diary:
      write_diary.write(line+"\n")
    print("Diary saved")
  elif choice==2:
    with open("diary.txt","r") as read_diary:
      for line in read_diary:
        print(line,end="")




