class Book:
    def __init__(self, title, year, author="Unknown"):
        self._title = title
        self._year = year
        self._author = author

    def set_title(self, new_title):
        self._title = new_title

    def set_year(self, new_year):
        self._year = new_year

    def get_author(self):
        return self._author
    def get_title(self):
        return self._title

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Year: {self._year}"

class DigitalLibrary:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, title):
        for book in self._books:
            if book.get_title() == title:
                self._books.remove(book)
                return f"Book titled '{title}' removed."
        return "Book not found."

    def print_books_by_author(self, author):
        found_books = [book for book in self._books if book.get_author() == author]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found by this author.")

    def __str__(self):
        return "\n".join(str(book) for book in self._books)
    
