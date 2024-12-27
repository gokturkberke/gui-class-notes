# I18N
# Basic implementation

import tkinter as tk
from tkinter import ttk
import langpack_v1 # Custom module to manage translations 

class AddNewGrade(tk.Tk):

    def __init__(self):
        super().__init__()
        self.i18n = langpack_v1.I18N("en") # Load language translations
        self.geometry("330x165+550+250")
        self.title(self.i18n.title) # Set the window title from the translations
        self.iconbitmap("python.ico")
        self.resizable(False, False)
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.lbl_fname = tk.Label(self, text=self.i18n.fname)
        self.lbl_lname = tk.Label(self, text=self.i18n.lname)
        self.lbl_grade = tk.Label(self, text=self.i18n.grade)

        self.txt_fname = ttk.Entry(self, width=35)
        self.txt_lname = ttk.Entry(self, width=35)
        self.txt_grade = ttk.Entry(self, width=35)

        self.btn_save = ttk.Button(self, text=self.i18n.save)

    def create_layout(self):
        self.columnconfigure(index=0, weight=1, uniform="eq")
        self.columnconfigure(index=1, weight=3, uniform="eq")
        self.rowconfigure(index=0, weight=1, uniform="eq")
        self.rowconfigure(index=1, weight=1, uniform="eq")
        self.rowconfigure(index=2, weight=1, uniform="eq")
        self.rowconfigure(index=3, weight=1, uniform="eq")

        self.lbl_fname.grid(column=0, row=0)
        self.lbl_lname.grid(column=0, row=1)
        self.lbl_grade.grid(column=0, row=2)

        self.txt_fname.grid(column=1, row=0)
        self.txt_lname.grid(column=1, row=1)
        self.txt_grade.grid(column=1, row=2)
        self.btn_save.grid(column=0, row=3, columnspan=2)


app = AddNewGrade()
