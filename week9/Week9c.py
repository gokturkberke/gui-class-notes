# GUI for editing records.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import dblib


class EditGrade(tk.Toplevel):

    def __init__(self, parent, rowid, gid, fname, lname, grade):
        super().__init__()
        self.geometry("330x165+600+300")
        self.title("Week 9")
        self.iconbitmap("python.ico")
        self.resizable(False, False)
        self.parent = parent
        self.rowid = rowid # ID of the Treeview item that is currently being edited.
        self.gid = gid
        self.fname = tk.StringVar(value=fname)
        self.lname = tk.StringVar(value=lname)
        self.grade = tk.IntVar(value=grade)
        self.db = dblib.GradeBookDatabase()
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.lbl_fname = tk.Label(self, text="First Name")
        self.lbl_lname = tk.Label(self, text="Last Name")
        self.lbl_grade = tk.Label(self, text="Grade")

        self.txt_fname = ttk.Entry(self, textvariable=self.fname, width=35)
        self.txt_lname = ttk.Entry(self, textvariable=self.lname, width=35)
        self.txt_grade = ttk.Entry(self, textvariable=self.grade, width=35)

        self.btn_update = ttk.Button(self, text="Update", command=self.update_values)

        self.txt_fname.focus_set()

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
        self.btn_update.grid(column=0, row=3, columnspan=2)

    def update_values(self):
        if len(self.lname.get()) == 0 or len(self.fname.get()) == 0:
            msg.showerror("Error", "Please fill out all fields in the form.")
            return
            
        try:
            # Update the database.
            self.db.update_grade(gid=self.gid, fname=self.fname.get(), lname=self.lname.get(), grade=self.grade.get())
            # Update the Treeview row (that is in the parent window).
            self.parent.tv.item(self.rowid, values=(self.gid, self.fname.get(), self.lname.get(), self.grade.get()))
            # Close the window.
            self.destroy()
        except (tk.TclError, OverflowError):
            msg.showerror("Error", "Unable to update data.")

