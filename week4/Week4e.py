# Menu with a check button

import tkinter as tk

def print_state(): #kullanici tarafindan checkbutton durumunu (secili mi secili degil mi ) yazdirir
    print(check_state.get()) 

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")
check_state = tk.BooleanVar()  # variable for the check button state
#check butonunun secili olup olmadigini saklayacak degisken
menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0)
file_menu.add_command(label="Open...", underline=0)
file_menu.add_separator()

sub_menu = tk.Menu(file_menu, tearoff=False)
sub_menu.add_command(label="Zoom in")
sub_menu.add_command(label="Zoom out")

file_menu.add_cascade(label="Editor", menu=sub_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.destroy, underline=1)

help_menu = tk.Menu(menubar, tearoff=False) #help_menu menusune bir checkbutton ekler
# Add a check button
help_menu.add_checkbutton(label="Send anonymous stats", onvalue=True, offvalue=False,
                          variable=check_state, command=print_state)
help_menu.add_separator()
help_menu.add_command(label="About...") #hakkinda secenegi help_menuya ekelr

menubar.add_cascade(label="File", menu=file_menu, underline=0)
menubar.add_cascade(label="Help", menu=help_menu)
#menuleri menubar a ekleme kodlari 
win.mainloop()
