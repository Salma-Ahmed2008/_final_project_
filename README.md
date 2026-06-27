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
- open browser and write the base_url with '/docs' to try it on swagger

How to run the CLI tool:
- open CMD and go to the project directory 
- write 'python cli\main.py'
- choose any option using arrows and enter