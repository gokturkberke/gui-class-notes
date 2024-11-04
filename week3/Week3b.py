import tkinter as tk

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# fill: Controls whether the widget should expand to fill the space allocated to it in the specified direction(s).
# expand: Controls whether the widget should be given extra space if the parent widget has any extra space available.
# anchor: Defines how the widget is positioned within its packing area (n, s, w, e, ne, ...).
label1.pack(ipadx=10, ipady=10, fill="y", expand=True)  # fill: none, x, y, both
label2.pack(ipadx=10, ipady=10, anchor="w")
label3.pack(ipadx=10, ipady=10, anchor="e")

win.mainloop()
