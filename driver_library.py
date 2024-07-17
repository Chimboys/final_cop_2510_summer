'''
Write the complete implementation for the Book and DigitalLibrary classes

Book contains title, year, author(by default "Unkwond"). Make all attributes protecred.
Created a seperate methods to change books title, year and accessor to get author name.
DigitalLibrary can add remove, print (print based on author name)

Make str for the book and digital library

Composition or inheritance?

Do you know how to call methods within a class?

How would initialize objects?

'''

from library import Book, DigitalLibrary
# Create instances of Book
book1 = Book("The Great Gatsby", 1925, "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", 1960, "Harper Lee")
book3 = Book("1984", 1949, "George Orwell")
book4 = Book("Beowulf", "8th-12th centuary")
book5 = Book("The Arabian Nights (One Thousand and One Nights)", "8th centuary")


# Create an instance of DigitalLibrary
myLibrary = DigitalLibrary()
#  Add books to the digital library
myLibrary.add_book(book1)
myLibrary.add_book(book2)
myLibrary.add_book(book3)
myLibrary.add_book(book4)
myLibrary.add_book(book5)



# Remove a book from the digital library
print(myLibrary.remove_book("1984"))  # Example of removing a book

# Print books by a specific author
print("Books by F. Scott Fitzgerald:")
myLibrary.print_books_by_author("F. Scott Fitzgerald")

# Display the entire digital library
print("\nCurrent Library Collection:")
print(myLibrary)













