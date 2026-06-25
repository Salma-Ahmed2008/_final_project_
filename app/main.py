from fastapi import FastAPI, HTTPException, status
from typing import List
from app.database import database
from app.schemas import BookCreate, BookResponse, BookUpdate

app = FastAPI(title = "Library API", description = "A simple API for managing books in a library", version = "1.0.0")

@app.get("/books", response_model=List[BookResponse], description="Retrieve a list of all books in the library", status_code=status.HTTP_200_OK)
def get_all_books():
    return list(database.values())

@app.get("/books/{book_id}", response_model=BookResponse, description="Retrieve a book by its ID", status_code=status.HTTP_200_OK)
def get_book(book_id: int):
    book = database.get(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@app.post("/books", response_model=BookResponse, description="Add a new book", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    new_id = max(database.keys(), default=0) + 1
    new_book = {"id": new_id, "title": book.title, "author": book.author, "available": True}
    database[new_id] = new_book
    return new_book

@app.patch("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update_book(book_id: int, payload: BookUpdate):
    task = database.get(book_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    if payload.title is not None:
        task["title"] = payload.title
    if payload.author is not None:
        task["author"] = payload.author
    if payload.available is not None:
        task["available"] = payload.available
    database[book_id] = task
    return task

@app.delete("/books/{book_id}",description="Delete a book", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    if book_id not in database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    del database[book_id]
    return None