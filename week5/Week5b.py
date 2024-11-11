# Event binding II (Mouse move)

import tkinter as tk
from tkinter import ttk

def click_event(event):
    # lbl.configure(text=event)

    button_name = "Unknown"
    if event.num == 1:
        button_name = "Left"
    elif event.num == 2:
        button_name = "Middle"
    elif event.num == 3:
        button_name = "Right"

    message = f"Clicked at: {event.x}, {event.y}.\n"
    message += f"Screen coordinates: {event.x_root}, {event.y_root}.\n"
    message += f"Event type: {event.type.name}.\n"
    message += f"Clicked button: {button_name}.\n"
    message += f"Button text: {event.widget["text"]}.\n"
    lbl.configure(text=message)

def mouse_enter(event): #fare butona girdiginde calisacak fonksiyon
    # event.widget["text"] = "Mouse entered"
    event.widget.configure(text="Mouse entered")

def mouse_leave(event): #fare butondan ciktiginda calisacak
    event.widget["text"] = "Mouse left"

def mouse_move(event): #dfare hareket ettihinde calisacak
    win.title(f"{event.x}, {event.y}") #fare hareket ederken koordinatlarini guncelliyoruz

win = tk.Tk()
win.title("Week 5")
win.geometry("400x250+500+200")
win.iconbitmap("python.ico")

btn_a = ttk.Button(win, text="Button A")
btn_b = ttk.Button(win, text="Button B")
lbl = ttk.Label(win, justify="center")

btn_a.pack(pady=(20, 0))
btn_b.pack(pady=20)
lbl.pack()

# B1-Motion (mouse drag with left button), B3-Motion (mouse drag with right button), MouseWheel, ...

btn_a.bind("<Button-1>", click_event) #sol fare tusuyla buton a tiklanirsa click event fonk. cagrilir
btn_b.bind("<Button-3>", click_event) #Sağ fare tuşu (Button-3) ile "Button B" butonuna tıklanırsa `click_event` fonksiyonunu cagiriyoruz
btn_a.bind("<Enter>", mouse_enter) #fare buton a ya girdiginde mouse entre fnk. cagirlir
btn_a.bind("<Leave>", mouse_leave) #ayni sekil a dan ciktiginda
win.bind("<Motion>", mouse_move) #hareket ettiginde

btn_a.focus()

win.mainloop()
