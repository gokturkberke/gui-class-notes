# Message and dialog boxes I

import tkinter as tk
from tkinter import messagebox as msg 

def print_state(): 
    print(check_state.get()) #check state degerini yazdirir(true ya da false) bu degisken send anonymous stats secenegi secildiginde guncellenir

def exit_app():
    dialog_result = msg.askyesno(title="Exit", message="Are you sure you want to exit?") #cikis yapmak istediginde kullanici bir onay penceresi gosterir
    # dialog_result = msg.askyesnocancel(title="Exit", message="Are you sure you want to exit?")
    if dialog_result: #evet derse true doner uygulama kapatilir
        win.destroy()

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

check_state = tk.BooleanVar() #send anonymous stats kutusu isaretli mi degil  mi diye takip ederiz

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False) #tearoff false ile menu ayrilamaz olur
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0, #new olustulur ve komutunua msg.showwarning atanir
                      command=lambda: msg.showwarning(title="Warning", #kullanici bu secenege tiklayinca bir uyari mesaji acilir
                                                      message="All unsaved progress will be lost."))
file_menu.add_command(label="Open...", underline=0,
                      command=lambda: msg.showerror(title="Error", #open secenegi icin hata mesaji acilir
                                                    message="Unable to open new file."))
file_menu.add_separator()

sub_menu = tk.Menu(file_menu, tearoff=False) #alt menu tanimlama
sub_menu.add_command(label="Zoom in")
sub_menu.add_command(label="Zoom out")

file_menu.add_cascade(label="Editor", menu=sub_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app, underline=1) #exit komutu eklenir exitapp fonksiyonuna baglidir

help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_checkbutton(label="Send anonymous stats", onvalue=True, offvalue=False,
                          variable=check_state, command=print_state) #bir isaret kutusu olur ve kyllanici kutuyu isaretleyince check state guncellenir
help_menu.add_separator()
help_menu.add_command(label="About...", #about help menu icine eklenir
                      command=lambda: msg.showinfo(title="About",
                                                   message="SEN4017 - GUI Programming with Python\nFall 2024"))

menubar.add_cascade(label="File", menu=file_menu, underline=0)
menubar.add_cascade(label="Help", menu=help_menu) #help menusu menubar menu cubuguna eklenir

win.mainloop()
