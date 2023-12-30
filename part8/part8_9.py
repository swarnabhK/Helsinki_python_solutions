"""Please write a function named books_of_genre(books: list, genre: str) which takes a list of objects of type Book and a string representing a genre as its arguments.

The function should return a new list, which contains the books with the desired genre from the original list"""

class Book:
    def __init__(self,name,author,genre,year) -> None:
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


def books_of_genre(books,genre):
    res = [book for book in books if book.genre==genre]
    return res
  
  

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

result = books_of_genre(books,"crime")
for book in result:
    print(f"{book.name}: {book.author}, genre: {book.genre}")