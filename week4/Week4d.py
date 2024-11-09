# Sub menu

import tkinter as tk

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

menubar = tk.Menu(win) #menu cubugunu olusturur
win.configure(menu=menubar) #pencereyi menu cubuguyla iliskilendirir

file_menu = tk.Menu(menubar, tearoff=False) #file menusunu olusturur
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0)
file_menu.add_command(label="Open...", underline=0)
file_menu.add_separator()

# Create a sub menu
sub_menu = tk.Menu(file_menu, tearoff=False) #Editor adi altinda verilen bir alt menu olsturur bu alt menu file_menu icinde yer alacak ve menu ogeleri barindiracak
sub_menu.add_command(label="Zoom in") #zoom in komutunu ekler alt menuye kullaniciya yakinlastirma secenegi sunar
sub_menu.add_command(label="Zoom out") #ayin sekil uzaklastirmali

# Add the sub menu under "Editor" (File > Editor)
file_menu.add_cascade(label="Editor", menu=sub_menu) #file menusune editor adli bir baslik ekler daha once olusturdugumuz sub_menu alt menusunu yerlestirir
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.destroy, underline=1) #exit komutunu ekler

help_menu = tk.Menu(menubar, tearoff=False) # help menusu olusturur
help_menu.add_command(label="About...")

menubar.add_cascade(label="File", menu=file_menu, underline=0) #file menusunu menu cubuguna ekler
menubar.add_cascade(label="Help", menu=help_menu) #help menusunu menu cubuguna ekler

win.mainloop()
