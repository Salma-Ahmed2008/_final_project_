import curses
from commands import book_commands

options = [
    "View Books",
    "View Book By ID",
    "Add Book",
    "Update Book",
    "Delete Book",
    "Exit"
]

def draw_menu(stdscr, selected):
    stdscr.addstr(0, 0, "LIBRARY SYSTEM")
    stdscr.addstr(1, 0, "-" * 30)
    for i, item in enumerate(options):
        if i == selected:
            stdscr.addstr(i+2, 0, "> " + item)
        else:
            stdscr.addstr(i+2, 0, "  " + item)

def menu(stdscr):
    selected = 0
    while True:
        stdscr.clear()
        draw_menu(stdscr, selected)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP:
            selected -= 1
        elif key == curses.KEY_DOWN:
            selected += 1
        elif key == curses.KEY_ENTER or key == 10:
            if selected == 0:
                book_commands.view_books(stdscr)
            elif selected == 1:
                book_commands.view_book_by_id(stdscr)
            elif selected == 2:
                book_commands.create_book(stdscr)
            elif selected == 3:
                book_commands.edit_book(stdscr)
            elif selected == 4:
                book_commands.remove_book(stdscr)
            elif selected == 5:
                break
            stdscr.addstr("Press Enter to continue")
            stdscr.getch()

        if selected < 0:
            selected = len(options)-1

        if selected >= len(options):
            selected = 0