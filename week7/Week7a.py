# GUI for inserting new records into the database.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import dblib #veritabani baglantisi icin gerekli


class AddNewGrade(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("330x165+550+250")
        self.title("Week 7")
        self.iconbitmap("python.ico")
        self.resizable(False, False)
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.grade = tk.IntVar()
        self.db = dblib.GradeBookDatabase() # Veritabanı bağlantısını başlatıyoruz.
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

        self.btn_save = ttk.Button(self, text="Save Grade", command=self.save_grade) # Notu kaydet butonu

        self.txt_fname.focus_set() # İlk isim giriş kutusuna odaklanıyoruz.

    def create_layout(self): #widgetlari yerlestirecegimiz yeri ayarliyoruz
        self.columnconfigure(index=0, weight=1, uniform="eq") #ilk sutunu ayarliyoruz
        self.columnconfigure(index=1, weight=3, uniform="eq")
        self.rowconfigure(index=0, weight=1, uniform="eq") #ilk satiri ayarliyoruz
        self.rowconfigure(index=1, weight=1, uniform="eq")
        self.rowconfigure(index=2, weight=1, uniform="eq")
        self.rowconfigure(index=3, weight=1, uniform="eq")

        self.lbl_fname.grid(column=0, row=0)
        self.lbl_lname.grid(column=0, row=1)
        self.lbl_grade.grid(column=0, row=2)

        self.txt_fname.grid(column=1, row=0)
        self.txt_lname.grid(column=1, row=1)
        self.txt_grade.grid(column=1, row=2)
        self.btn_save.grid(column=0, row=3, columnspan=2) # Kaydet butonunu konumlandırıyoruz. iki sutun genisliginde olacak sekilde

    def save_grade(self): # Kaydet butonuna tıklanınca çalışan fonksiyon
        if len(self.lname.get()) == 0 or len(self.fname.get()) == 0:
            msg.showerror("Error", "Please fill out all fields in the form.")
            return #isim ya da soy isim alani os ise error fonderir

        try: # Veritabanına notu kaydetmeye çalışır.
            self.db.save_grade(fname=self.fname.get(), lname=self.lname.get(), grade=self.grade.get())
            msg.showinfo("Done", "Grade saved.")
            self.reset_text_boxes() # Giriş kutularını sıfırlar
            self.txt_fname.focus_set() # İlk isim giriş kutusuna odaklanır.
        except (tk.TclError, OverflowError):
            msg.showerror("Error", "Unable to save data.")

    def reset_text_boxes(self): #giris kutularini sifirlayan fonksiyon
        self.fname.set("") #ilk ismi temizler
        self.lname.set("")
        self.grade.set(0)


app = AddNewGrade() # Ana sınıfı çağırarak uygulamayı başlatıyoruz.

#focus_set() ozelligi : Bu özellik olmadan, kullanıcı ilgili widget'a tıklamadıkça yazı yazmaya başlayamaz. Örneğin, bir metin giriş kutusuna focus_set() eklendiğinde, kullanıcı pencere açıldığında direkt olarak yazmaya başlayabilir. Eklenmediğinde ise, kullanıcı önce giriş kutusuna tıklamalıdır.

