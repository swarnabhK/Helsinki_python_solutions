# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user.



whom = input("Whom should I sign this to: ")
where = input("Where shall I save it: ")

with open(where,"w") as file:
  file.write(f"Hi {whom}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")