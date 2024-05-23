# Write your solution here:


class Series:
  def __init__(self,name,seasons,genres):
    self.title = name
    self.season = seasons
    self.genres = genres
    self.rating = 0
    self.no_ratings = 0
  
  
  def rate(self,rate):
    self.rating+=rate
    self.no_ratings+=1

  def __str__(self):
    r = f"{self.no_ratings} ratings, average {(self.rating/self.no_ratings):.1f} points" if self.no_ratings else "no ratings"
    return f"{self.title} ({self.season} seasons)"+'\n'+f"genres: {", ".join(g for g in self.genres)}"+'\n'+r

def minimum_grade(rating,series_list):
  #will search through the list of series and return a list of series satisfying the minimum rating
  res = []
  for s in series_list:
    if s.rating>=rating:
      res.append(s)
  return res

def includes_genre(genre,series_list):
  res = []
  for s in series_list:
    if genre in s.genres:
      res.append(s)
  return res

s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)
