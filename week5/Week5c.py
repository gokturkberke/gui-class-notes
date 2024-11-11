# Event binding III (Keyboard)

import tkinter as tk
from tkinter import ttk

def key_press(event): #bir tusa basildiginda tetiklenir
    lbl2["text"] = event.keysym  # event.keycode #basilan tusun ismini lbl2 adli etiketin metni olarak ayarlar

def focus_gained(event):
    lbl2["text"] = "Focus gained"

def focus_lost(event):
    lbl2["text"] = "Focus lost"

def return_key(event): #return tusuna bastiginda tetikklenir(enter) entry kutusundaki mesaji alir ve buyuk harfe donusturur
    lbl2["text"] = entry.get().upper()

def key_combination(event): #bu belirli bir tus kombinasyonu mesela(ctrl a ) basildiginda tetiklenir
    lbl2["text"] = "Key combination pressed"

win = tk.Tk()
win.title("Week 5")
win.geometry("400x250+500+200")
win.iconbitmap("python.ico")

lbl1 = ttk.Label(win, text="Enter your text and press <Return>")
entry = ttk.Entry(win, width=30) #metnin girilebilecegi giris kutusu
btn = ttk.Button(win, text="Button") #islevsiz bir buton
lbl2 = ttk.Label(win, text="", font=("Consolas", 12))  # ("Times", 16, "bold", "italic") klavye etkilesimlerinin sonucunu gosteren etiket

lbl1.pack(pady=20)
entry.pack(pady=(0, 20))
btn.pack(pady=(0, 20))
lbl2.pack()

entry.bind("<Key>", key_press)  # KeyPress, KeyRelease, F1, F2, ...
entry.bind("<FocusIn>", focus_gained) #metine tiklandiginda focus gained yazar
entry.bind("<FocusOut>", focus_lost) #farkli biseye mesela butona basinca focus lost yazar
entry.bind("<Return>", return_key) #entera basinca return key fonksiyonu calisir
win.bind("<Control-a>", key_combination) # Control-Shift-A, ...

win.mainloop()
