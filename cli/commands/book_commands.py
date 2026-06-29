from services.book_service import *
from utils.formatter import *
import curses

def view_books(stdscr):
    books = get_all_books()
    height, width = stdscr.getmaxyx()
    pad = curses.newpad(1000, width)
    print_books(pad, books)
    position = 0
    while True:
        pad.refresh(position,0,0,0,height - 1,width - 1)
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            position += 1
        elif key == curses.KEY_UP:
            position -= 1
        elif key == 10:
            break
        if position < 0:
            position = 0
    stdscr.clear()


def view_book_by_id(stdscr):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Book ID: ")
    stdscr.refresh()
    book_id = stdscr.getstr().decode()
    curses.noecho()
    book = get_book(book_id)
    stdscr.clear()
    print_book(stdscr, book)
    stdscr.refresh()
    stdscr.getch()

def create_book(stdscr):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Title: ")
    stdscr.refresh()
    title = stdscr.getstr().decode()
    stdscr.addstr(1, 0, "Author: ")
    stdscr.refresh()
    author = stdscr.getstr().decode()
    curses.noecho()
    book = add_book(title, author)
    stdscr.clear()
    print_book(stdscr, book)
    stdscr.refresh()

def edit_book(stdscr):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Book ID: ")
    stdscr.refresh()
    book_id = stdscr.getstr().decode()
    data = {}
    stdscr.addstr(1, 0, "New title (Enter to skip): ")
    stdscr.refresh()
    title = stdscr.getstr().decode()

    if title:
        data["title"] = title
    stdscr.addstr(2, 0, "New author (Enter to skip): ")
    stdscr.refresh()
    author = stdscr.getstr().decode()

    if author:
        data["author"] = author
    stdscr.addstr(3, 0, "Available true/false (Enter to skip): ")
    stdscr.refresh()
    available = stdscr.getstr().decode()

    if available:
        data["available"] = available.lower()=="true"
    curses.noecho()
    stdscr.clear()
    book = update_book(book_id,data)
    print_book(stdscr, book)
    stdscr.refresh()
    stdscr.getch()
    stdscr.clear()

def remove_book(stdscr):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Book ID: ")
    stdscr.refresh()
    book_id = stdscr.getstr().decode()
    curses.noecho()
    stdscr.clear()
    delete_book(book_id)
    stdscr.addstr(1, 0, "Deleted successfully")
    stdscr.refresh()
    curses.noecho()
    stdscr.getch()
    stdscr.clear()