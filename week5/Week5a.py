# Event binding I (Mouse click)

import tkinter as tk
from tkinter import ttk

def click_event(event): #event gerceklesince cagrilir
    # lbl.configure(text=event)

    button_name = "Unknown"
    if event.num == 1:
        button_name = "Left"
    elif event.num == 2:
        button_name = "Middle"
    elif event.num == 3:
        button_name = "Right"

    message = f"Clicked at: {event.x}, {event.y}.\n" #butonun neresine tiklama koordinatlari
    message += f"Screen coordinates: {event.x_root}, {event.y_root}.\n" #ekranin tamamina gore fare konumu
    message += f"Event type: {event.type.name}.\n" #olay turu buttonpress veya buttonrelease
    message += f"Clicked button: {button_name}.\n" #tikladigimiz butonun ismi
    message += f"Button text: {event.widget["text"]}.\n" #tiklanan dugme metni
    lbl.configure(text=message) #lbl etiketinin metnini bu mesajla gunceller

win = tk.Tk()
win.title("Week 5")
win.geometry("400x250+500+200")
win.iconbitmap("python.ico")

btn_a = ttk.Button(win, text="Button A")
btn_b = ttk.Button(win, text="Button B")
lbl = ttk.Label(win, justify="center") #verielcek bilgi metnini ortalar

btn_a.pack(pady=(20, 0)) #ustten 20px bosluk
btn_b.pack(pady=20) #hem ust hem alt 20px bosluk
lbl.pack() #dugmeleri ekrana ekledik

# Button, Button-1, Button-2, Button-3, Double-Button, Double-Button-1, ButtonRelease, ButtonRelease-1, ...

btn_a.bind("<Button>", click_event) #dugmeye herhangi bir fare dugmesiyle tiklanirsa click event fonksiyonu cagrilir
btn_b.bind("<ButtonRelease-3>", click_event) #sag fare dugmesi birakildiginda button release cagrilir

btn_a.focus() #buton a ilk odaklanmayi saglar

win.mainloop()
