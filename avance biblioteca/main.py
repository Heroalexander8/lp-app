
# main.py
import tkinter as tk
from interface.app_interface import LibraryApp

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

    
