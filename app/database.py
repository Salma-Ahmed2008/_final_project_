import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

db = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def get_books():
    response = (
        db.table("books")
        .select("*")
        .execute()
    )
    return response.data

def get_book(book_id):
    response = (
        db.table("books")
        .select("*")
        .eq("id", book_id)
        .execute()
    )
    return response.data

def create_book(book):
    response = (
        db.table("books")
        .insert(book)
        .execute()
    )
    return response.data

def update_book(book_id, book):
    response = (
        db.table("books")
        .update(book)
        .eq("id", book_id)
        .execute()
    )
    return response.data

def delete_book(book_id):
    response = (
        db.table("books")
        .delete()
        .eq("id", book_id)
        .execute()
    )
    return response.data