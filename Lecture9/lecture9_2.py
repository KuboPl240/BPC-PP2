from abc import ABC, abstractmethod

# Base class for all Media
class Media(ABC):
    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year

    @abstractmethod
    def display_info(self):
        pass

# Class for Books
class Book(Media):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def display_info(self):
        return f"Book: '{self.title}' by {self.creator} ({self.year}), {self.pages} pages."

# Class for Vinyl Records
class VinylRecord(Media):
    def __init__(self, title, artist, year, duration):
        super().__init__(title, artist, year)
        self.duration = duration

    def display_info(self):
        return f"Vinyl Record: '{self.title}' by {self.creator} ({self.year}), Duration: {self.duration} min."

# Class for Movies
class Movie(Media):
    def __init__(self, title, director, year, length):
        super().__init__(title, director, year)
        self.length = length

    def display_info(self):
        return f"Movie: '{self.title}' directed by {self.creator} ({self.year}), Length: {self.length} min."

# Create instances
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)
vinyl = VinylRecord("Thriller", "Michael Jackson", 1982, 42)
movie = Movie("Inception", "Christopher Nolan", 2010, 148)

# Display information
print(book.display_info())
print(vinyl.display_info())
print(movie.display_info())
