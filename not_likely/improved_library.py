#create a journal that is the same as a book but it has area (f.e, chemistry , physics) and it has issue)
# You are given , another class called 

from library import Book, DigitalLibrary

class Journal(Book):
    def __init__(self, title, author, year , issue, area):
        super().__init__(title, author, year)
        self._issue = issue
        self._area = area
    def __str__(self):
        return super().__str__() + f", Issue: {self._issue}"

class LibraryStatistics:
    def __init__(self):
        self.books_added = 0
        self.books_removed = 0

    def update_books_added(self):
        self.books_added += 1

    def update_books_removed(self):
        self.books_removed += 1

    def print_statistics(self):
        print(f"Books Added: {self.books_added}, Books Removed: {self.books_removed}")

class ManagedDigitalLibrary(DigitalLibrary, LibraryStatistics):
    def __init__(self):
        #better to specify which class is reffered in constructor 
        DigitalLibrary.__init__(self)
        LibraryStatistics.__init__(self)

    def add_book(self, book):
        super().add_book(book)  # Call the add_book method from DigitalLibrary
        self.update_books_added()

    def remove_book(self, title):
        result = DigitalLibrary.remove_book(self,title)  # Call the remove_book method from DigitalLibrary
        if "removed" in result:
            self.update_books_removed()
        return result
