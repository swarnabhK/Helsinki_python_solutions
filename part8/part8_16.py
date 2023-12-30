class Series:
    def __init__(self,title,no_of_seasons,list_genres) -> None:
        self.title = title
        self.no_of_seasons = no_of_seasons
        self.list_genres = list_genres
        self.ratings = 0
        self.rating = 0
    def rate(self,rating):
        self.rating+=rating
        self.ratings+=1
    def __str__(self):
        genres = ", ".join(self.list_genres)
        average = self.rating/self.ratings if self.ratings>0 else 0
        s = f"{self.title} ({self.no_of_seasons} seasons)"+"\n"+f"genres: {genres}"+"\n"+f"{self.ratings} ratings, average {average} points"
        return s

def minimum_grade(rating,series_list):
    res = []
    for series in series_list:
        if (series.rating/series.ratings)>=rating:
            res.append(series)
    return res        

def includes_genre(genre,series_list):
    res = []
    for series in series_list:
        if(genre in series.list_genres):
            res.append(series)
    return res

# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# dexter.rate(4)
# dexter.rate(5)
# dexter.rate(5)
# dexter.rate(3)
# dexter.rate(0)
# print(dexter)

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


