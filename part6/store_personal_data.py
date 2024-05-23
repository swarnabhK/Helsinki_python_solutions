# Write your solution here
# Please write a function named store_personal_data(person: tuple), which takes a tuple containing some identifying information as its argument.

# The tuple contains the following elements:

# Name (string)
# Age (integer)
# Height (float)
# This should be processed and written into the file people.csv. The file may already contain some data; the new entry goes to the end of the file. The data should be written in the format

# name;age;height



def store_personal_data(person):
  name,age,height = person
  line = f"{name};{age};{height}"
  with open("people.csv","a") as file:
    file.write(line+"\n")

person = "Paul Paulson", 37, 175.5
store_personal_data(person)