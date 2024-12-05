class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

author1 = Author("Ben Carson")
# print(author1.name)

book1 = Book("Think Big", author1.name)
print(f"The book {book1.title} was Authored by {book1.author}")