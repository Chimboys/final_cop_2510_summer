#List comprehension
books = [
    {"title": "Book A", "author": "Author X", "year": 1999, "pages": 300},
    {"title": "Book B", "author": "Author Y", "year": 2005, "pages": 450},
    {"title": "Book C", "author": "Author Z", "year": 2010, "pages": 200},
    {"title": "Book D", "author": "Author W", "year": 2000, "pages": 150},
    {"title": "Book E", "author": "Author V", "year": 2020, "pages": 500},
]

'''
Problem Statement:
Given a list of dictionaries
where each dictionary contains information about a book (title, author, year of publication, and number of pages),
perform the following tasks using list and dictionary comprehension:

1)Filter books published after 2000.
2) Create a list of tuples where each tuple contains titles and authors of these books.
3) Count the total number of pages of books published after 2000.
'''








#Q1
books_after_2000 = [book for book in books if book["year"] > 2000]



#Q2
title_and_author_after_2000 = [(book["title"], book["author"]) for book in books_after_2000]





# Count the total number of pages of books published after 2000
total_pages_after_2000 = sum(book["pages"] for book in books_after_2000)

print(total_pages_after_2000)
