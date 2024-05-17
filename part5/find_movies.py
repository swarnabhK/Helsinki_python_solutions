# Please write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise. The function should formulate a new list, which contains only the movies whose title includes the word searched for. Capitalisation is irrelevant here. A search for ana should return a list containing both Anaconda and Management.

def find_movies(db,search_term):
  search_term = search_term.lower()
  res = []
  for movie in db:
    words = movie['name'].split()
    for word in words:
      if search_term in word.lower():
        res.append(movie)
  return res


database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

my_movies = find_movies(database, "python")
print(my_movies)
