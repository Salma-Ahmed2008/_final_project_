def print_book(pad, book):
    pad.addstr("\nBOOK DETAILS\n")
    pad.addstr("-" * 40 + "\n")
    pad.addstr(f"ID: {book['id']}\n")
    pad.addstr(f"Title: {book['title']}\n")
    pad.addstr(f"Author: {book['author']}\n")
    pad.addstr(f"Available: {book['available']}\n")
    pad.addstr("-" * 40 + "\n")



def print_books(pad, books):
    pad.addstr("\nBOOK LIST\n")
    pad.addstr("-" * 40 + "\n")
    for book in books:
        pad.addstr(f"ID: {book['id']}\n")
        pad.addstr(f"Title: {book['title']}\n")
        pad.addstr(f"Author: {book['author']}\n")
        pad.addstr(f"Available: {book['available']}\n")
        pad.addstr("-" * 40 + "\n")