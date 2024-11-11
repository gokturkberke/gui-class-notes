# Progressbar with threading

import tkinter as tk
from tkinter import ttk
from time import sleep
import threading

# Flag to control the running thread
stop_thread = False

def start_progressbar():
    # Runs the progressbar continuously
    progressbar1.start(interval=10)  # milliseconds

def stop_progressbar():
    # Stops the running progressbar
    global stop_thread
    stop_thread = True # Set the flag to stop the thread
    progressbar1.stop()

def run_progressbar():
    # Runs the progressbar based on a given range
    global stop_thread
    stop_thread = False # Reset the stop flag
    progressbar1["value"] = 0
    progressbar1["maximum"] = 100

    # Start a new thread to update the progress bar
    threading.Thread(target=progressbar_task).start()

def progressbar_task():
    # This runs in a separate thread.
    for i in range(0, 101, 20):
        if stop_thread: # Check the flag to stop the thread
            break
        print(i)
        progressbar1["value"] = i
        progressbar1.update()
        sleep(1) # Simulate a time-consuming task (1-second delay)

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
