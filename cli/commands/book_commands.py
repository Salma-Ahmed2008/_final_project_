from services.book_service import *
from utils.formatter import *

def view_books():
    books = get_all_books()
    print_books(books)

def view_book_by_id():
    book_id = input("Book ID: ")
    book = get_book(book_id)
    print_book(book)

def create_book():
    title = input("Title: ")
    author = input("Author: ")
    book = add_book(title, author)
    print_book(book)

def edit_book():
    book_id = input("Book ID: ")
    data = {}
    title = input("New title (Enter skip): ")

    if title:
        data["title"] = title
    author = input("New author (Enter skip): ")

    if author:
        data["author"] = author
    available = input("Available true/false (Enter skip): ")

    if available:
        data["available"] = available.lower()=="true"
    book = update_book(book_id,data)
    print_book(book)

def remove_book():
    book_id = input("Book ID: ")
    delete_book(book_id)
    print("Deleted successfully")