def print_book(book):
    print("\nBOOK DETAILS")
    print("-"*40)
    print(f"ID: {book['id']}")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Available: {book['available']}")
    print("-"*40)

def print_books(books):
    print("\nBOOK LIST")
    print("-"*40)
    for book in books:
        print(f"""
ID: {book['id']}
Title: {book['title']}
Author: {book['author']}
Available: {book['available']}
""")
    print("-"*40)