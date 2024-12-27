# I18N
# Change the active language at runtime

import tkinter as tk
from tkinter import ttk
import langpack_v1

class AddNewGrade(tk.Tk):

    def __init__(self):
        super().__init__()
        self.selected_language = tk.StringVar(value="en") # Set the default language
        self.i18n = langpack_v1.I18N(self.selected_language.get()) # Load translations for the selected language
        self.geometry("330x165+550+250")
        self.title(self.i18n.title)
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

        # Add a context menu
        self.context_menu = tk.Menu(self, tearoff=False)

        # Add language names to the context menu
        self.context_menu.add_radiobutton(label="English",
                                          value="en",
                                          variable=self.selected_language,
                                          command=lambda : self.reload_gui_text())
        self.context_menu.add_radiobutton(label="Türkçe",
                                          value="tr",
                                          variable=self.selected_language,
                                          command=lambda : self.reload_gui_text())

        # Bind mouse right-click event to display the context menu
        self.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event): # Sağ tıklama menüsünü fare imlecinin bulunduğu yerde açar.
        self.context_menu.post(event.x_root, event.y_root)

    def reload_gui_text(self): # Seçilen dile göre arayüz metinlerini yeniden yükler ve günceller.
        self.i18n = langpack_v1.I18N(self.selected_language.get()) # Yeni dil çevirilerini yükler.
        self.title(self.i18n.title)
        self.lbl_fname.configure(text=self.i18n.fname)
        self.lbl_lname.configure(text=self.i18n.lname)
        self.lbl_grade.configure(text=self.i18n.grade)
        self.btn_save.configure(text=self.i18n.save)

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
