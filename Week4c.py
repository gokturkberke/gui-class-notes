# Menu with multiple items and accelerators

import tkinter as tk

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0)
file_menu.add_command(label="Open...", underline=0)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.destroy, underline=1)

help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_command(label="About...")

menubar.add_cascade(label="File", menu=file_menu, underline=0)
menubar.add_cascade(label="Help", menu=help_menu)

win.mainloop()
