from dataclasses import field
import sys
import requests

base_url = "http://127.0.0.1:8000"


def get_all_books():
    response = requests.get(f"{base_url}/books")
    response.raise_for_status()
    return response.json()


def get_book(book_id):
    response = requests.get(f"{base_url}/books/{book_id}")
    response.raise_for_status()
    return response.json()


def add_book(title, author):
    response = requests.post(
        f"{base_url}/books",
        json={"title": title, "author": author}
    )
    response.raise_for_status()
    return response.json()


def delete_book(book_id):
    response = requests.delete(f"{base_url}/books/{book_id}")
    response.raise_for_status()
    return {"message": "Book deleted successfully"}

def update_book(book_id, data):
    response = requests.patch(
        f"{base_url}/books/{book_id}",
        json=data
    )
    response.raise_for_status()
    return response.json()

# simple formatter
def print_book(book):
    print("\nBOOK DETAILS")
    print("-" * 40)
    print(f"ID: {book['id']}")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Available: {book['available']}")
    print("-" * 40)


def print_books(books):
    print("\nBOOK LIST")
    print("-" * 40)
    for book in books:
        print(f"ID: {book['id']}\n Title: {book['title']}\n Author: {book['author']}\n Available: {book['available']}")
    print("-" * 40)

# main
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python cli/cli.py <command> [<args>]")
        print("Commands: list, get, add, delete, update")
        return
    
    command = args[0]
    try:
        if command == "list":
            books = get_all_books()
            print_books(books)
        elif command == "get":
            if len(args) < 2:
                print("Usage: get <book_id>")
                return
            book = get_book(args[1])
            print_book(book)
        elif command == "add":
            if len(args) < 3:
                print("Usage: add <book_title> <author_name>")
                return
            new_book = add_book(args[1], args[2])
            print("\nBook added successfully")
            print_book(new_book)
        elif command == "delete":
            if len(args) < 2:
                print("Usage: delete <book_id>")
                return
            delete_book(args[1])
            print("\nBook deleted successfully")
        elif command == "update":
            if len(args) < 2:
                print("Usage: update <book_id> --field value")
                return
            book_id = args[1]
            data = {}
            i = 2
            while i < len(args):
                if args[i] == "--title":
                    data["title"] = args[i+1]
                    i+=2
                elif args[i] == "--author":
                    data["author"] = args[i+1]
                    i+=2
                elif args[i] == "--available":
                    data["available"] = args[i+1].lower() == "true"
                    i+=2
                else:
                    i+=1

            if not data:
                print("Nothing to update. Use --title, --author, or --available.")
                return
            updated_book = update_book(book_id, data)
            print("\nBook updated successfully")
            print_book(updated_book)
        else:
            print(f"Unknown command: {command}")
    except requests.exceptions.RequestException as e:
        print(f"an error occurred: {e}")


if __name__ == "__main__":
    main()