Book Management System (FastAPI + CLI)

-- overview --
simple Book Management System built using FastAPI as a backend API and a python CLI tool as a client interface

The system allows users to:
- add books
- view all books
- get a specific book
- update books
- delete books

How to run the Backend:
- open the terminal in main.py
- run this command: uvicorn backend.main:app --reload
- open browser and write the local URL with '/docs' to try it on swagger

How to run the CLI tool:
- open CMD and go to the project directory 
- write 'python cli\cli.py' with any of these commands:
-- list                                             # to list all books
-- add "book title" "author name"                   # to add a new book
-- get book_id                                      # to get a book with its id
-- update book_id "new title" "new author" true     # to update a book
-- delete book_id                                   # to delete a book with its id