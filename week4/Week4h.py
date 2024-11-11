# Spinbox belirli bir degeri secmek icin yukari ve asagi oklarla gezilebilen bir giris kutusudur

import tkinter as tk
from tkinter import ttk

def click_handler():#spinboxtan secilen degeri alir
    ttk.Label(win, text=spin_value.get()).pack()  #bu da pencere de label olarak goruntuler

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

spin_value = tk.StringVar()
spin_values = tuple(str(i) for i in range(1, 20, 3))
# wrap: True makes the Spinbox cycle through the values.
# spinbox1 = ttk.Spinbox(win, from_=0, to=10, wrap=True, state="readonly", textvariable=spin_value)
# spinbox1 = ttk.Spinbox(win, values=("1", "3", "5", "7"), wrap=True, textvariable=spin_value)
# spinbox1 = ttk.Spinbox(win, values=spin_values, wrap=True, textvariable=spin_value)
spinbox1 = ttk.Spinbox(win, values=spin_values, wrap=True, textvariable=spin_value, command=click_handler)
#win spinboxin bulunacagi ana pencere
#values=spin_values: Spinbox'ta görüntülenecek değerler spin_values değişkeninde belirtilmiştir.
#wrap=True: Kullanıcının Spinbox’ın sonuna veya başına geldiğinde başa veya sona dönmesini sağlar (değerler döngü şeklinde gösterilir).
#textvariable=spin_value: Seçilen değerin spin_value değişkeninde saklanmasını sağlar.
spinbox1.pack() #spinboxi pencereye yerlestirir

win.mainloop()
