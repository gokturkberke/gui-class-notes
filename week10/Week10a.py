# Install customtkinter: https://customtkinter.tomschimansky.com/
# Basic CTk GUI

import customtkinter as ctk


def change_appearance():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


win = ctk.CTk()
win.title("Week 10")
win.geometry("300x200")

lbl = ctk.CTkLabel(win, text="GUI Programming with Python", fg_color=("orange", "green"), corner_radius=20)
#corner radius make corners rounded bigger number more rounded corner
lbl.pack(pady=20)

btn = ctk.CTkButton(win, text="Change Appearance", command=change_appearance)
btn.pack()

win.mainloop()