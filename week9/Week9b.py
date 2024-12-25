# GUI for listing database content (Treeview with scrollbar and event bindings).

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import dblib
import Week9c


class ListGrades(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("450x200+550+250")
        self.title("Week 9")
        self.iconbitmap("python.ico")
        self.db = dblib.GradeBookDatabase()
        self.create_widgets()
        self.create_layout()
        self.list_grades()
        self.mainloop()

    def create_widgets(self):
        # Create a Treeview widget.
        # selectmode: extended(default), browse, none
        self.tv = ttk.Treeview(self, height=10, show="headings") #max gosterilecek satir sayisi 10
        self.tv["columns"] = ("id", "fname", "lname", "grade")
        self.tv["selectmode"] = "browse"

        # Add headings for each column.
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("fname", text="First Name", anchor="center")
        self.tv.heading("lname", text="Last Name", anchor="center")
        self.tv.heading("grade", text="Grade", anchor="center")

        # Configure each column.
        self.tv.column("id", anchor="center", width=45, stretch=False) #stretch false pencere boyutuna gore esnemez(degismez)
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="center", width=135)

        # Add a vertical scrollbar to the Treeview.
        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview) #command = selftv.yview aydırma çubuğu hareket ettirildiğinde, Treeview’in dikey kaydırma fonksiyonu (yview) çağrılır.
        self.tv.configure(yscrollcommand=self.tv_scroll.set)

        # Bind the F1 key to the function that shows the average grade.
        self.bind("<F1>", self.show_average)

        # Bind the Treeview selection event to the item_select function.
        self.tv.bind("<<TreeviewSelect>>", self.item_select)

        # Bind the Delete key to the function that deletes the selected row.
        self.tv.bind("<Delete>", self.delete_grade)

        # Bind a double-click event to open the edit window.
        self.tv.bind("<Double-1>", self.show_edit_window)

    def create_layout(self):
        self.tv.pack(fill="both", expand=True) #treeview pencere boyutuna gore genisler ve cerceve degistirildiginde otomatik olarak yeniden boyutlanir
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")
        #anchor ne = Kaydırma çubuğunun yerleştirme noktasını sag ust olarak belirtir ,Bu, kaydırma çubuğunu oraya doğru hizalar.
        #relheight=1 kaydirma cubugu pencerenin yuksekligi kadar olur

    def list_grades(self):
        grades = self.db.get_grades()
        for g in grades:
            # Populate the Treeview by adding values to the end of it.
            # self.tv.insert(parent="", index="end", values=(g[0], g[1], g[2], g[3]))
            self.tv.insert(parent="", index="end", values=g)

    def show_average(self, event):
        result = self.db.get_count_and_average()

        if result[0] == 0:  # Check the total number of grades
            msg_content = "The database is empty."
        else:
            msg_content = (f"Number of recorded grades: {result[0]}\n\n"
                           f"The average: {round(result[1], 1)}")

        msg.showinfo(title="Count and Average", message=msg_content)

    def item_select(self, event):
        # print(self.tv.selection())
        for i in self.tv.selection():
            # print(self.tv.item(i))
            print(self.tv.item(i)["values"]) #satirdaki tum degerleri alir

    def delete_grade(self, event):
        if len(self.tv.selection()) == 0: # Do nothing if no rows are selected.
            return
            
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"] # Get the values of the selected all rows
                self.db.delete_grade(selected_row[0])
                self.tv.delete(i)

    def show_edit_window(self, event):
        region = self.tv.identify("region", event.x, event.y) #Tiklamanin hangi kordinatlarda yapildigi degerini alir
        if region != "cell": #eger tiklama bir hucrede degilse cikis yap
            return

        selected_row_id = self.tv.selection()[0] # Get the ID of the selected row.
        selected_grade_row = self.tv.item(selected_row_id)["values"] # Get the values of the selected row.
        self.edit_selected = Week9c.EditGrade(parent=self,
                                              rowid=selected_row_id,
                                              gid=selected_grade_row[0],
                                              fname=selected_grade_row[1],
                                              lname=selected_grade_row[2],
                                              grade=selected_grade_row[3])
        self.edit_selected.grab_set() #Yeni açılan pencereyi modal hale getirir. 
        #Bu, kullanıcı diğer pencerelere tıklayamadan önce düzenleme penceresini kapatmasını zorunlu kılar.


app = ListGrades()
