import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
color = colorchooser.askcolor()
root.configure(background=color[1])
tk.mainloop()