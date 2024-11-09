# Menu with multiple items and accelerators

import tkinter as tk

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False) #file menusunu olusturur ve menuden bagimsiz yeni bir pencere acmasini engeller kullanicinin
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0) # new komutunu file menusune ekler ve accelerator kodu ile ctrl +n tuslarina basildiginda new komutunun calisacagini belirtir
file_menu.add_command(label="Open...", underline=0) #open... komutunu file menusune ekler alti cizili yapmaz
file_menu.add_separator() #menu ogeleri arasina bir yatay cizgi yerlestirir
file_menu.add_command(label="Exit", command=win.destroy, underline=1) #exit ekler e harfini alti cizili yapar ve kullanici buna tikaldiginda pencerenin kapanmasini saglar

help_menu = tk.Menu(menubar, tearoff=False) #help menusu olusturur
help_menu.add_command(label="About...") #help menusune about komutu eklenmesini saglar

menubar.add_cascade(label="File", menu=file_menu, underline=0)
menubar.add_cascade(label="Help", menu=help_menu) #underline=0  yazmadigimiz icin otomatik olarak h nin altini cizer(windowsta)
#bu iki satirin amaci menu cubuguna file ve help menulerini eklemektir bu satir olmamasi durumunda menuler eklenmez
#label = file kodu file metni menu basligi olarak gorunur
#menu=file_menu kodu ise file menusunun icinde hangi seceneklerin yer alacagini belirtir (file_menuyu daha once olusturduk icinde new open gbibi komutlari barindirir)
win.mainloop()
