import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def button_handler():
    win.destroy()

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x240+100+100")

notebook1 = ttk.Notebook(win)
notebook1.pack(pady=20)

tab1 = ttk.Frame(notebook1)
tab2 = ttk.Frame(notebook1)

tab1.pack()
tab2.pack()

notebook1.add(tab1, text="Tab 1")
notebook1.add(tab2, text="Tab 2")

scrolled_text1 = ScrolledText(tab1, width=30, height=10, wrap="word")  # none, char, word
scrolled_text1.pack(fill="both")

label1 = ttk.Label(tab2, text="This is tab 2.")
button1 = ttk.Button(tab2, text="Exit", command=button_handler)
label1.pack(pady=50)
button1.pack(pady=10)

win.mainloop()
