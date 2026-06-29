from fastapi import FastAPI
from app.schemas import BookCreate, BookUpdate
from app.database import (
    get_books,
    get_book,
    create_book,
    update_book,
    delete_book
)

app = FastAPI(
    title="Book Management API"
)

@app.get("/books")
def list_books():
    return get_books()

@app.get("/books/{book_id}")
def book(book_id: int):
    return get_book(book_id)

@app.post("/books")
def add_book(book: BookCreate):
    return create_book(book.model_dump())

@app.patch("/books/{book_id}")
def edit_book(book_id: int, book: BookUpdate):
    return update_book(
        book_id,
        book.model_dump(exclude_none=True)
    )

@app.delete("/books/{book_id}")
def remove_book(book_id: int):
    return delete_book(book_id)