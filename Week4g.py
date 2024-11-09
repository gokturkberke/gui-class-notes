# Message and dialog boxes II

import tkinter as tk
from tkinter import messagebox as msg
from tkinter import filedialog as fd

def open_file():
    file_filter = (
        ("All types", "*.*"),
        ("Text file", "*.txt"),
        ("PDF file", "*.pdf")
    )
    selected_file = fd.askopenfilename(filetypes=file_filter)
    tk.Label(win, text=selected_file).pack()

def print_state():
    print(check_state.get())

def exit_app():
    dialog_result = msg.askyesno(title="Exit", message="Are you sure you want to exit?")
    # dialog_result = msg.askyesnocancel(title="Exit", message="Are you sure you want to exit?")
    if dialog_result:
        win.destroy()

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

check_state = tk.BooleanVar()

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0,
                      command=lambda: msg.showwarning(title="Warning", message="All unsaved progress will be lost."))
file_menu.add_command(label="Open...", underline=0,
                      command=open_file)
file_menu.add_separator()

sub_menu = tk.Menu(file_menu, tearoff=False)
sub_menu.add_command(label="Zoom in")
sub_menu.add_command(label="Zoom out")

file_menu.add_cascade(label="Editor", menu=sub_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app, underline=1)

help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_checkbutton(label="Send anonymous stats", onvalue=True, offvalue=False,
                          variable=check_state, command=print_state)
help_menu.add_separator()
help_menu.add_command(label="About...",
                      command=lambda: msg.showinfo(title="About",
                                                   message="SEN4017 - GUI Programming with Python\nFall 2024"))

menubar.add_cascade(label="File", menu=file_menu, underline=0)
menubar.add_cascade(label="Help", menu=help_menu)

win.mainloop()
