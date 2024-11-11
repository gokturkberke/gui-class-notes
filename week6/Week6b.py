# Toplevel (show-hide main)

import tkinter as tk
from tkinter import ttk


def open_second_window():
    win.withdraw() # Hide the main window (ana pencereyi gizler) kullanici sadece ikinci pencereyi gorur
    global win2 #baska yerlerde kullanabilmek icin global tanimladik
    win2 = tk.Toplevel(win) # Ana pencereden bağımsız yeni bir "Toplevel" pencere açar (yeni pencere).
    win2.title("Second Window")
    win2.geometry("300x200+550+250")
    ttk.Label(win2, text="Second Window").pack(pady=(20, 0)) # İkinci pencereye bir etiket (Label) ekler ve aralarına boşluk bırakır.
    ttk.Button(win2, text="Close", command=close_second_window).pack(pady=(20, 0))
    # Set the protocol for handling the window close button (title bar close) # İkinci pencereyi kapatırken main pencereyi geri getiren bir fonksiyon belirleriz.
    win2.protocol("WM_DELETE_WINDOW", close_second_window)# Pencereyi kapatmaya çalıştığında close_second_window fonksiyonunu çalıştırır.


def close_second_window():
    win.deiconify() # Show the main window again #ana pencereyi tekrar gorunur hale getirir
    win2.destroy() # Close the second window


win = tk.Tk()
win.title("Week 6")
win.geometry("300x300+500+200")
win.iconbitmap("python.ico")

btn1 = ttk.Button(win, text="Open Second Window", command=open_second_window)
btn2 = ttk.Button(win, text="Close", command=win.destroy)

btn1.pack(pady=(20, 0))
btn2.pack(pady=(20, 0))

win.mainloop()
#Bu kod, ana pencerenin gizlenip gösterilmesini ve ikinci pencerenin kapatılmasının ardından ana pencerenin tekrar görünmesini sağlar.
#week6a da ikinci pencere bagimsiz bir pencere olarak acilir ve ana pencere gizlenmezdi bu kodda İkinci pencere açıldığında ana pencere gizlenir, ve ikinci pencereyi kapattığınızda ana pencere tekrar görünür hale gelir.