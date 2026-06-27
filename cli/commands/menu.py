import os
import msvcrt
from commands.book_commands import *

options = [
    "View Books",
    "View Book By ID",
    "Add Book",
    "Update Book",
    "Delete Book",
    "Exit"
]

def draw_menu(selected):
    print("LIBRARY SYSTEM")
    print("-"*30)
    for i,item in enumerate(options):
        if i == selected:
            print("> "+item)
        else:
            print("  "+item)

def run_menu():
    selected = 0
    while True:
        os.system("cls")
        draw_menu(selected)
        key = msvcrt.getch()

        if key == b'\xe0':
            key = msvcrt.getch()

            if key == b'H':
                selected -= 1

            elif key == b'P':
                selected += 1

        elif key == b'\r':
            os.system("cls")

            if selected == 0:
                view_books()

            elif selected == 1:
                view_book_by_id()

            elif selected == 2:
                create_book()

            elif selected == 3:
                edit_book()

            elif selected == 4:
                remove_book()

            elif selected == 5:
                exit()
            input("\nPress Enter...")

        if selected < 0:
            selected = len(options)-1

        if selected >= len(options):
            selected = 0