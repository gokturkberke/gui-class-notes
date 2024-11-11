import tkinter as tk  
from tkinter import ttk  


# İkinci pencereyi oluşturacak olan sınıf
class SecondWindow(tk.Toplevel):

    def __init__(self, parent):  # İkinci pencere başlatılır, parent ana pencereyi temsil eder.
        super().__init__()  # Toplevel sınıfının __init__ metodunu çağırıyoruz.
        self.parent = parent  # Ana pencereyi kaydediyoruz.
        self.title("Second Window")  
        self.geometry("300x200+600+300") 
        self.iconbitmap("python.ico")  
        self.create_widgets()  # Pencere widget'larını oluşturuyoruz.
        self.create_layout()  # Widget'ları pencereye yerleştiriyoruz.
        self.protocol("WM_DELETE_WINDOW", self.close_window)  # Pencereyi kapatma işlevini bağlıyoruz.

    def create_widgets(self):  # Widget'ları oluşturduğumuz fonksiyon
        self.lbl1 = ttk.Label(self, text="Second Window", font=("Tahoma", 16))  # Bir etiket oluşturuyoruz.
        self.lbl2 = ttk.Label(self, text="Enter your message and press <Return>.")  # Bir başka etiket oluşturuyoruz.
        self.entry1 = ttk.Entry(self)  # Bir metin giriş kutusu oluşturuyoruz.
        self.btn1 = ttk.Button(self, text="Close", command=self.close_window)  # Kapatma butonunu oluşturuyoruz.

        self.entry1.bind("<Return>", self.return_key)  # Kullanıcı <Return> tuşuna basarsa return_key fonksiyonunu çağırır.
        self.entry1.focus_set()  # Giriş kutusuna odaklanıyoruz, böylece hemen yazılabilir.

    def create_layout(self):  
        self.lbl1.pack(pady=(20, 0))  
        self.lbl2.pack(pady=(20, 0)) 
        self.entry1.pack(pady=(20, 0))  
        self.btn1.pack(pady=(20, 0))  

    def return_key(self, event):  # Kullanıcı <Return> tuşuna basarsa çalışacak fonksiyon
        self.parent.lbl2.configure(text=f"Message from the second window: {self.entry1.get()}")  # Ana pencerenin lbl2 etiketini güncelliyoruz.
        self.close_window()  

    def close_window(self):  # Pencereyi kapatma fonksiyonu
        self.destroy()  



win = tk.Tk()  
win.title("Main Window")  
win.geometry("300x300+500+200") 
win.iconbitmap("python.ico")  

# İkinci pencereyi açacak butonu oluşturuyoruz.
btn_open = ttk.Button(win, text="Open Second Window", command=lambda: SecondWindow(win))  # Lambda fonksiyonu ile SecondWindow sınıfını çağırıyoruz.
btn_open.pack(pady=20)  # Butonu yerleştiriyoruz.

win.mainloop() 

