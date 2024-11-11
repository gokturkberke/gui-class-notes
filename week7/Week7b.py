# GUI for listing database content (Treeview).

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
        self.create_layout() # Layout'u oluşturuyoruz.
        self.list_grades()
        self.mainloop()

    def create_widgets(self):
        # Create a Treeview widget.
        # selectmode: extended(default), browse, none # selectmode: Seçim modunu ayarlıyoruz (browse ile tek bir öğe seçilebilir).
        self.tv = ttk.Treeview(self, height=10, show="headings")
        self.tv["columns"] = ("id", "fname", "lname", "grade")  # Sütun başlıklarını belirliyoruz.
        self.tv["selectmode"] = "browse" # Tek bir seçim yapılabilmesini sağlıyoruz.

        # Add headings for each column. #her sutun icin baslik ekliyoruz
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("fname", text="First Name", anchor="center")
        self.tv.heading("lname", text="Last Name", anchor="center")
        self.tv.heading("grade", text="Grade", anchor="center")

        # Configure each column. Her sütunun genişliğini ve hizasını ayarlıyoruz.
        self.tv.column("id", anchor="center", width=45, stretch=False) # ID sütununu ortalıyoruz ve sabit genişlik veriyoruz.
        self.tv.column("fname", anchor="w", width=135) # isim
        self.tv.column("lname", anchor="w", width=135) #soy isimi sola hizaliyoruz
        self.tv.column("grade", anchor="center", width=135)

    def create_layout(self):
        self.tv.pack(fill="both", expand=True) # Treeview'ı pencerenin tamamını kaplayacak şekilde yerleştiriyoruz.

    def list_grades(self):
        grades = self.db.get_grades() # Veritabanından notları alıyoruz.
        for g in grades:
            # Populate the Treeview by adding values to the end of it.
            # self.tv.insert(parent="", index="end", values=(g[0], g[1], g[2], g[3]))
            self.tv.insert(parent="", index="end", values=g)


app = ListGrades()
