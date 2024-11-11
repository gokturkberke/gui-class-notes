import tkinter as tk
from tkinter import ttk
import Week6h # Second window


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Week 6")
        self.geometry("300x200+550+250")
        self.iconbitmap("python.ico")
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.lbl1 = ttk.Label(self, text="Main Window", font=("Tahoma", 16))
        self.lbl2 = ttk.Label(self) # Diğer bir etiket oluşturuyoruz (boş).
        self.btn1 = ttk.Button(self, text="Open Second Window", command=self.open_new_window)# İkinci pencereyi açacak buton.
        self.btn2 = ttk.Button(self, text="Close", command=self.destroy)

    def create_layout(self): #widgetlari pencereye yerlestiriyoruz
        self.lbl1.pack(pady=(20, 0))
        self.btn1.pack(pady=(20, 0))
        self.btn2.pack(pady=(20, 0))
        self.lbl2.pack(pady=(20, 0))

    def open_new_window(self):
        self.win2 = Week6h.SecondWindow(parent=self) # Week6h modülünden SecondWindow sınıfını çağırıyoruz.
        self.win2.grab_set() # İkinci pencereyi mod (ana pencereyi etkisiz hale getirme) yapıyoruz.


app = MainWindow()
 #ana pencere acilir bir buton icerir bu butonla ikinci pencere acilir ve acildiktan sonra ilk pencere gecici olarak etkisiz hale gelir
 #ikinci pencere bir mesaj yazdirir enter tusuyla ana pencereye gonderir.