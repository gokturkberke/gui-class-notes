import tkinter as tk
from tkinter import ttk

def button_handler():
    label1.configure(text=entry1.get() + " " + selected_combo_item.get() + " " + selected_radio_item.get())

def checkbox_handler():
    if checkbox_state.get() == "Enabled":
        button1.configure(state="normal")
        label1.configure(text="Button enabled.")
    else:
        button1.configure(state="disabled")
        label1.configure(text="Button disabled.")

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x330+100+100")
selected_combo_item = tk.StringVar(value="Option 2")
selected_radio_item = tk.StringVar()
checkbox_state = tk.StringVar(value="Enabled")

frame1 = ttk.LabelFrame(win, text="Some GUI Widgets")
label1 = ttk.Label(frame1, text="Label")
entry1 = ttk.Entry(frame1, width=30)
combo1 = ttk.Combobox(frame1, width=15, textvariable=selected_combo_item, state="readonly")
combo1["values"] = ("Option 1", "Option 2")
radio1 = ttk.Radiobutton(frame1, text="Item 1", value="A", variable=selected_radio_item)  # command=callback_func
radio2 = ttk.Radiobutton(frame1, text="Item 2", value="B", variable=selected_radio_item)
checkbox1 = ttk.Checkbutton(frame1, text="Enable button", onvalue="Enabled", offvalue="Disabled",
                            variable=checkbox_state, command=checkbox_handler)
button1 = ttk.Button(frame1, text="Send", command=button_handler)  # state="disabled" (normal, disabled, active)

frame1.pack(fill="both", expand=True, padx=10, pady=10)
label1.pack(pady=10)
entry1.pack(pady=10)
combo1.pack(pady=10)
radio1.pack(pady=10)
radio2.pack(pady=10)
checkbox1.pack(pady=10)
button1.pack(pady=10)

win.mainloop()
