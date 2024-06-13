
import tkinter as tk
from database.db_manager import DatabaseManager
from interface.gui import LibraryGUI


def main():
    db_path = '/mnt/data/Biblioteca'
    db_manager = DatabaseManager(db_path)

    root = tk.Tk()
    app = LibraryGUI(root, db_manager)
    root.mainloop()


if __name__ == "__main__":
    main()
