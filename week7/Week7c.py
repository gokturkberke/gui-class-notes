# GUI for listing database content (Treeview with scrollbar).

import tkinter as tk
from tkinter import ttk
import dblib


class ListGrades(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("450x200+550+250")
        self.title("Week 7")
        self.iconbitmap("python.ico")
        self.db = dblib.GradeBookDatabase()
        self.create_widgets()
        self.create_layout()
        self.list_grades()
        self.mainloop()

    def create_widgets(self):
        # Create a Treeview widget.
        # selectmode: extended(default), browse, none
        self.tv = ttk.Treeview(self, height=10, show="headings")
        self.tv["columns"] = ("id", "fname", "lname", "grade")
        self.tv["selectmode"] = "browse" #Only one item can be selected at a time.
        #extended = multiple row selection
        #none = no row selection

        # Add headings for each column.
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("fname", text="First Name", anchor="center")
        self.tv.heading("lname", text="Last Name", anchor="center")
        self.tv.heading("grade", text="Grade", anchor="center")

        # Configure each column.
        self.tv.column("id", anchor="center", width=45, stretch=False)
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="center", width=135)

        # Add a vertical scrollbar to the Treeview. Treeview bileşenine dikey bir kaydırma çubuğu ekliyoruz.
        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview) #kaydirma cubugunu olusturuyoruz
        self.tv.configure(yscrollcommand=self.tv_scroll.set) # Kaydırma çubuğunu Treeview bileşenine bağlıyoruz.

    def create_layout(self):
        self.tv.pack(fill="both", expand=True)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne") # Kaydırma çubuğunu Treeview'in sağına konumlandırıyoruz.
        


    def list_grades(self):
        grades = self.db.get_grades()
        for g in grades:
            # Populate the Treeview by adding values to the end of it. # Treeview bileşenini, veritabanından alınan her bir veriyle dolduruyoruz.
            # self.tv.insert(parent="", index="end", values=(g[0], g[1], g[2], g[3]))
            self.tv.insert(parent="", index="end", values=g)


app = ListGrades()
