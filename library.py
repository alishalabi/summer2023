"""
Concept taken from https://www.youtube.com/watch?v=1qw5ITr3k9E

Implement a cloud based book application (think kindle)
Users have a library of books
Users can set a book to their active book
Application remembers where user left off in a given book
The application only displays one page at time

"""

# Assumption - no empty books
class Book:
    def __init__(self, title, author, corpus, current_page=0, ):
        self.title = title
        self.author = author
        self.current_page = corpus
        # key value pairs -> {page_number, string}
        self.full_book =  {}
        for i in range(len(corpus)):
            page = {i: corpus[i]}
            self.full_book.update(page)

class Reader:
    def __init__(self, all_books=[]):
        self.all_books = all_books
        self.current_book = all_books[0]
        self.current_page = all_books[0].current_page

    def set_book(self, book):
        self.current_book = book

# Assumption - book is formatted as an array of strings
test_corpus = ["Once upon a time there was a bear", "That bear was cool",
                "The bear did great in the interview!", "The bear got the job"]

test_book = Book("My Book", "Ali", test_corpus)

print(test_book.full_book)
