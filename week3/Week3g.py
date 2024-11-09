import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText #cok satirli metin alanlarina dikey bir kaydirma cubugu ekler

def button_handler(): #exite tiklandiginda bu fonksiyon calisir
    win.destroy() #bu komut ile pencere kapanir

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x240+100+100")

notebook1 = ttk.Notebook(win) #bu yapi sayesinde pencere icerisinde sekmeler yaratilabilir
notebook1.pack(pady=20) #notebook widgetini yerlestirir ve 20 px yukardan bosluk birakir

tab1 = ttk.Frame(notebook1)
tab2 = ttk.Frame(notebook1)

tab1.pack()#sekme cercevesi yerlestirme kodu
tab2.pack() 

notebook1.add(tab1, text="Tab 1")
notebook1.add(tab2, text="Tab 2")

scrolled_text1 = ScrolledText(tab1, width=30, height=10, wrap="word")  #Metin alani ekler(wrap="word" metnin kelimelere gore satir sonunda kaydirilmasiin saglar) none, char, word
scrolled_text1.pack(fill="both") #mevcutolan tum alani doldurcak skeilde yerlestirilir

label1 = ttk.Label(tab2, text="This is tab 2.")
button1 = ttk.Button(tab2, text="Exit", command=button_handler) #tab2 sekmesine buton ekler butona basildiginda fonksiyon cagrilarak pencere kapatilir
label1.pack(pady=50)
button1.pack(pady=10)

win.mainloop()


#wrap="none" : Metin kutusunda satır kaydırma yapılmaz(alt satira gecmez yani). Kullanıcı, metin kutusunun içeriğini kaydırmak için yatay kaydırma çubuğunu kullanmak zorundadır.
#wrap = "char" : Metin kutusu içinde her karakter kaydırıldığında yeni bir satıra geçilir. Yani, bir karakter kaydırıldığında bir sonraki satıra geçilir. Bu, kelime kesintileri oluşturabilir.
#wrap="word" :Bu, metnin kelime bazında kaydırılmasını sağlar. Yani, bir kelime tamamlanmadan yeni bir satıra geçmez. Bu, metin kutusunda daha okunabilir bir düzen sağlar.