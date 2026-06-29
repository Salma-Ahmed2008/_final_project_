from commands.menu import menu
import curses

if __name__ == "__main__":
    curses.wrapper(menu)