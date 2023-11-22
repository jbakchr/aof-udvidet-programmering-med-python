"""
Exercise 1 - Recap from 2nd night lecture

Create a class called "BookStore" that:
- has a class attribute called "books" set to an empty list
- takes a "name" and a "max_books" argument in the constructor function (i.e. "__init__" method)

Create a class called "Book" that:
- takes a "title", "author" and "price" as arguments
- has a method for returning the price of the book

Create a method in the "BookStore" class that'll add a "Book" to its list of books - but only its
max of books isn't reached yet.

Create a method called "get_total_price" in the "BookStore" class that'll return the total price
from its list of books.

Create an instance of your "BookStore" class.

Create as many instances of your "Book" class as you like and add them to your "BookStore" class.

Lastly, call the "get_total_price" method on your "BookStore" and print some text about the total price of the books.
"""


class BookStore:
    books = []

    def __init__(self, name, max_books):
        self.name = name
        self.max_books = max_books

    def add_book(self, book):
        if len(self.books) != self.max_books:
            self.books.append(book)

    def get_total_price(self):
        total = 0
        for book in self.books:
            total += book.get_price()
        return total


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_price(self):
        return self.price


bs = BookStore("My Book Store", 5)

b1 = Book("Den gamle mand og havet", "Ernest Hemingway", 150)
b2 = Book("Processen", "Franz Kafka", 129)
b3 = Book("idioten", "En eller anden russer ..", 399)

bs.add_book(b1)
bs.add_book(b2)
bs.add_book(b3)

print(bs.get_total_price())
