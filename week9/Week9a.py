# GUI for inserting new records into the database.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import dblib


class AddNewGrade(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("330x165+550+250")
        self.title("Week 9")
        self.iconbitmap("python.ico")
        self.resizable(False, False)
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.grade = tk.IntVar()
        self.db = dblib.GradeBookDatabase()
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.lbl_fname = tk.Label(self, text="First Name")
        self.lbl_lname = tk.Label(self, text="Last Name")
        self.lbl_grade = tk.Label(self, text="Grade")

        self.txt_fname = ttk.Entry(self, textvariable=self.fname, width=35)
        self.txt_lname = ttk.Entry(self, textvariable=self.lname, width=35)
        self.txt_grade = ttk.Entry(self, textvariable=self.grade, width=35)

        self.btn_save = ttk.Button(self, text="Save Grade", command=self.save_grade)

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
        self.btn_save.grid(column=0, row=3, columnspan=2)

    def save_grade(self):
        if len(self.lname.get()) == 0 or len(self.fname.get()) == 0:
            msg.showerror("Error", "Please fill out all fields in the form.")
            return
            
        try:
            self.db.save_grade(fname=self.fname.get(), lname=self.lname.get(), grade=self.grade.get())
            msg.showinfo("Done", "Grade saved.")
            self.reset_text_boxes() # Reset the text boxes after saving the grade.
            self.txt_fname.focus_set() # Set the focus back to the first name text box.
        except (tk.TclError, OverflowError):
            msg.showerror("Error", "Unable to save data.")

    def reset_text_boxes(self): #clear the input fields
        self.fname.set("")
        self.lname.set("")
        self.grade.set(0)


app = AddNewGrade() #create the AddNewGrade object
