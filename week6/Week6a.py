# Toplevel

import tkinter as tk
from tkinter import ttk


def open_second_window(): #bu fonksiyon yeni bir ikinci pencere acmak icin kullanilir
    win2 = tk.Toplevel(win) # Ana pencereden bağımsız yeni bir "Toplevel" pencere açar (yeni pencere).
    win2.title("Second Window")
    win2.geometry("300x200+550+250")
    # win2.grab_set()  # Restricts all user interactions to this window only (modal window). # Bu satır, ikinci pencereyi modal yapar; yani, kullanıcı sadece bu pencereyle etkileşime girebilir (yorumda olduğu için çalışmaz).
    ttk.Label(win2, text="Second Window").pack(pady=(20, 0)) #pencereye bir etiket ekler ve aralarina bosluk birakir
    ttk.Button(win2, text="Close", command=win2.destroy).pack(pady=(20, 0)) #ikinci pencereye bir kapama butonu ekler


win = tk.Tk()
win.title("Week 6")
win.geometry("300x300+500+200")
win.iconbitmap("python.ico")

btn1 = ttk.Button(win, text="Open Second Window", command=open_second_window) # "Open Second Window" butonunu ekler, tıklandığında open_second_window() fonksiyonu çalışır.
btn2 = ttk.Button(win, text="Close", command=win.destroy)

btn1.pack(pady=(20, 0))
btn2.pack(pady=(20, 0))

win.mainloop()
