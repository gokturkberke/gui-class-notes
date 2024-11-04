import tkinter as tk
import random

def click_handler():
    random_number = random.randint(1, 100) #1 ile 100 dahil random sayi
    label1.configure(foreground="red") #label1 eiketinin metin rengini kirmizi yapar
    label1.configure(text=f"Random number: {random_number}") #rastgele sayiyi gunceller

win = tk.Tk()
win.title("Week 2")
win.iconbitmap("python.ico") #week2nin yaninda gorsel dosya olusturur
#olmasa da olur fakat uygulamanin gorsel kimligi azalir
win.geometry("300x100+100+100") #300 px genislik 100 px yukseklik

label1 = tk.Label(win, text="Click the button to generate a number!") #baslangicta kullanciya bilgi vermek icin kullanilir
label1.pack() #etiketi pencereye ekler ve yerlestirir

button1 = tk.Button(win, text="Generate Random Number", command=click_handler) 
button1.pack() #command click handler butona tiklanildiginda click handler fonksiyonunun caslimasini saglar
#button1.pack butonu pencereye ekler ve yerlestirir
win.mainloop() #donguyu baslatir
