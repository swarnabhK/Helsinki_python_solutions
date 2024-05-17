# Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.
# The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.
# name
# director
# year
# runtime
# The values attached to these keys are given as arguments to the function.


def add_movie(db,name,director,year,runtime):
  dic = {}
  dic['name'],dic['director'],dic['year'],dic['runtime'] =  name, director, year, runtime
  db.append(dic)


database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(database)