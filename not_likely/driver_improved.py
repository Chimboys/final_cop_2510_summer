#Improved runner
# Create a journal that is the same as a book but it has area (f.e, chemistry , physics) and it has issue
# You are given library statitics class use it and DigitalLibrary class that counts how many books were added and removed
# It has str method that calls string method of its parents
from library import Book, DigitalLibrary
from improved_library import Journal, ManagedDigitalLibrary

# Create instances of Journal
journal1 = Journal("Journal of Advanced Chemistry", "Marie Curie", 2021, 1, "Chemistry")
journal2 = Journal("Physics Today", "Albert Einstein", 2020, 5, "Physics")
journal3 = Journal("Modern Biology", "Charles Darwin", 2022, 2, "Biology")

# Create an instance of ManagedDigitalLibrary
managedLibrary = ManagedDigitalLibrary()

# Add the Journal instances to the ManagedDigitalLibrary
managedLibrary.add_book(journal1)
managedLibrary.add_book(journal2)
managedLibrary.add_book(journal3)

# Remove a Journal from the ManagedDigitalLibrary
managedLibrary.remove_book("Physics Today")

# Step 6: Print statistics about the library's operations
managedLibrary.print_statistics()

# Step 7: Display the entire ManagedDigitalLibrary collection
print("\nCurrent Managed Digital Library Collection:")
print(managedLibrary)

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

class DigitalLibrary:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, title):
        for book in self._books:
            if book._title == title:
                self._books.remove(book)
                return f"Book titled '{title}' removed."
        return "Book not found."

    def print_books_by_author(self, author):
        found_books = [book for book in self._books if book._author == author]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found by this author.")

    def __str__(self):
        return "\n".join(str(book) for book in self._books)


    
    
