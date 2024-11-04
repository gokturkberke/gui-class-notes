import tkinter as tk

win = tk.Tk()
win.title("Week 2")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")
win.resizable(False, False)

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="#ffffff")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

label1.pack()
label2.pack()
label3.pack()

win.mainloop()
