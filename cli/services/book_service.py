import requests

base_url = "https://finalproject-production-66d0.up.railway.app"

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
        json={
            "title": title,
            "author": author
        }
    )
    response.raise_for_status()
    return response.json()

def delete_book(book_id):
    response = requests.delete(f"{base_url}/books/{book_id}")
    response.raise_for_status()

def update_book(book_id, data):
    response = requests.patch(f"{base_url}/books/{book_id}",json=data)
    response.raise_for_status()
    return response.json()