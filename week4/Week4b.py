# Simple menu

import tkinter as tk

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

menubar = tk.Menu(win) #ana pencere icinde(win bir menu cubugu olusturur)
win.configure(menu=menubar) #win penceresine menu cubugunu ekler

file_menu = tk.Menu(menubar, tearoff=False) #menu cubugu altinda file menusu olusturur
#tearoff=false ayari menuden yeni bir pencere acilmasini engeller
file_menu.add_command(label="Exit", command=win.destroy)
#file menusune secenek ekler bu secenek exit etiketine sahip olacak ve tiklaninca win.destroy fonk calistiracak

# underline: specifies the character index that will be underlined
# for keyboard shortcut (press <Alt> for Windows)
menubar.add_cascade(label="File", menu=file_menu, underline=0)
#file menusunu menu cubuguna ekler
#label="File": Menü başlığını "File" olarak ayarlar
#menu=file_menu: Daha önce oluşturulan file_menu (çıkış menüsü) menüsünü bu başlık altına ekler.
#underline=0: "File" menüsünde ilk harfi (F) altı çizili yapmaz. Eğer underline=0 yerine underline=1 olsaydı, "F" harfi altı çizili olurdu
#sadece win icin gecerli underline kodu
win.mainloop()
