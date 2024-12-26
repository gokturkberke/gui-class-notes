# Install ttkbootstrap: https://ttkbootstrap.readthedocs.io/en/latest/
# Basic ttkbootstrap GUI

import ttkbootstrap as ttk

win = ttk.Window(themename="superhero")
win.geometry("500x500")
win.title("Week 11")

btn1 = ttk.Button(win, text="Button 1", bootstyle="success") #buton stili success
btn1.pack(padx=15, pady=(30, 15)) #15 sag sol 30 ust 15 alt

btn2 = ttk.Button(win, text="Button 2", bootstyle=("info", "outline")) #outline kenarlari cizgili bir tema
btn2.pack(padx=15, pady=15) 

cbtn1 = ttk.Checkbutton(win, text="Check button", bootstyle="warning-round-toggle")
cbtn1.pack(padx=15, pady=15)

date_entry = ttk.DateEntry(win, bootstyle="success", width=10)
date_entry.pack(padx=15, pady=15)

win.mainloop()
