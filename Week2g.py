import tkinter as tk
import random

def click_handler():
    random_number = random.randint(1, 100)
    label1.configure(foreground="red")
    label1.configure(text=f"Random number: {random_number}")

win = tk.Tk()
win.title("Week 2")
win.iconbitmap("python.ico")
win.geometry("300x100+100+100")

label1 = tk.Label(win, text="Click the button to generate a number!")
label1.pack()

button1 = tk.Button(win, text="Generate Random Number", command=click_handler)
button1.pack()

win.mainloop()
