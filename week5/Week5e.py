# Progressbar

import tkinter as tk
from tkinter import ttk
from time import sleep

def start_progressbar():
    # Runs the progressbar continuously
    progressbar1.start(interval=10)  # milliseconds

def stop_progressbar():
    # Stops the running progressbar
    progressbar1.stop()

def run_progressbar():
    # Runs the progressbar based on a given range
    progressbar1["value"] = 0
    progressbar1["maximum"] = 100
    # Increments the progressbar 20 by 20 every 1 second
    for i in range(0, 101, 20):
        print(i)
        progressbar1["value"] = i
        progressbar1.update()
        sleep(1)  # Simulate a time-consuming task (1-second delay)

win = tk.Tk()
win.title("Week 5")
win.geometry("300x200+500+200")
win.iconbitmap("python.ico")

progressbar1 = ttk.Progressbar(win, orient="horizontal",  length=250, mode="determinate")  # determinate, indeterminate
progressbar1.pack(pady=20)

ttk.Button(win, text="Start", command=start_progressbar).pack(pady=(0, 10))
ttk.Button(win, text="Stop", command=stop_progressbar).pack(pady=(0, 10))
ttk.Button(win, text="Run", command=run_progressbar).pack()

win.mainloop()
