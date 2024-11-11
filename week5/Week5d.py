# Context menu

import tkinter as tk
from tkinter import ttk
from datetime import datetime

def show_context_menu(event): #bu fonksiyon sag tiklama(buton 3) olayinda cagrilir
    # Places the context menu to the (x,y) coordinate of the mouse.
    # event.x_root, event.y_root returns the coordinate of the mouse relative to the top left corner of the screen.
    # event.x, event.y returns the coordinate of the mouse relative to the top left corner of the widget.
    context_menu.post(event.x_root, event.y_root) #fare tiklamnin ekranin (top-left corner) korrdinatlarina gore pozisyonu alir ve menuyu bu koordinata gore yerelstirir
    #yani nerde sag tiklarsak orda cikar yapabilkeceklerimiz

def show_date(): #gecerli tarihi alir
    # ttk.Label(win, text=str(datetime.now()), font=("Consolas", 16)).pack(pady=(10, 0))
    labels.append(ttk.Label(win, text=datetime.now().strftime("%d.%m.%Y - %H:%M:%S"), font=("Consolas", 16)))  #gun ay yil saat dakika seklinde
    labels[-1].pack(pady=(10, 0)) #yeni eklenen etiketi ekranda gosterir ustten 10px bosluk

def clear(): #tum etiketleri siler
    for label in labels:
        label.destroy()
    labels.clear()

win = tk.Tk()
win.title("Week 5")
win.geometry("300x300+500+200")
win.iconbitmap("python.ico")
labels = [] #etiketlerin toplanacagi bos liste

context_menu = tk.Menu(win, tearoff=False)
context_menu.add_command(label="Show date and time", command=show_date)
context_menu.add_command(label="Clear", command=clear)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=win.destroy)

win.bind("<Button-3>", show_context_menu) #sag butona tiklaninca gelir ekrana fonksiyonlar

win.mainloop()
