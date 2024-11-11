# GUI for listing database content (Treeview with scrollbar and event bindings).

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
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
        self.tv = ttk.Treeview(self, height=10, show="headings") #height goruntulenecek max satir sayisi
        self.tv["columns"] = ("id", "fname", "lname", "grade") #headings sadece basliklarin gorunmesini saglar satir numaralarini gostermez
        self.tv["selectmode"] = "browse"

        # Add headings for each column.
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("fname", text="First Name", anchor="center")
        self.tv.heading("lname", text="Last Name", anchor="center")
        self.tv.heading("grade", text="Grade", anchor="center")

        # Configure each column.
        self.tv.column("id", anchor="center", width=45, stretch=False) #stretch false sutunun ozelliklerini ayarlar
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="center", width=135)

        # Add a vertical scrollbar to the Treeview.
        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)

        # Bind the F1 key to the function that shows the average grade.
        self.bind("<F1>", self.show_average) # F1 tuşuna basıldığında ortalamayı gösteren fonksiyonu bağlar.

        # Bind the Treeview selection event to the item_select function.
        self.tv.bind("<<TreeviewSelect>>", self.item_select) # Treeview öğesinin seçilmesi durumunda item_select fonksiyonunu bağlar.

        # Bind the Delete key to the function that deletes the selected row.
        self.tv.bind("<Delete>", self.delete_grade) # Delete tuşuna basıldığında delete_grade fonksiyonunu bağlar.

    def create_layout(self):
        self.tv.pack(fill="both", expand=True)  # Treeview widget'ını pencereye yerleştirir.
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne") # Scrollbar'ı pencerenin sağ üst köşesine yerleştirir.

    def list_grades(self): # Veritabanından notları alır ve Treeview widget'ına ekler.
        grades = self.db.get_grades()
        for g in grades:
            # Populate the Treeview by adding values to the end of it.
            # self.tv.insert(parent="", index="end", values=(g[0], g[1], g[2], g[3]))
            self.tv.insert(parent="", index="end", values=g)

    def show_average(self, event): # F1 tuşuna basıldığında, veritabanındaki notların sayısını ve ortalamasını gösterir.
        result = self.db.get_count_and_average()
        msg_content = (f"Number of recorded grades: {result[0]}\n\n"
                       f"The average: {round(result[1], 1)}")
        msg.showinfo(title="Count and Average", message=msg_content)

    def item_select(self, event):
        # print(self.tv.selection())
        for i in self.tv.selection():
            # print(self.tv.item(i))
            print(self.tv.item(i)["values"]) # Seçilen öğenin değerlerini konsola yazdırır.

    def delete_grade(self, event): #delete tusunua basinca cagrilir
        if len(self.tv.selection()) == 0: # Do nothing if no rows are selected. # Hiçbir öğe seçilmediyse, işlem yapmaz.
            return
            
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row?")
        if answer: # Eğer kullanıcı silmeyi onaylarsa
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_grade(selected_row[0]) # Seçilen satırı veritabanından siler (ID'yi kullanarak).
                self.tv.delete(i) # Seçilen satırı Treeview'dan siler.


app = ListGrades()
