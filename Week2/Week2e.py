import tkinter as tk

win = tk.Tk() #tk.Tk ifadesi ana pencereyi olusturur
win.title("Week 2") #pencere basligi
win.geometry("300x300+100+100") #300x300 pencerenin genisligini ve yuksekligin
#+100 +100 ise pencerenin sol ust kosesinden 100 piksel saga ve 100 piksel asagi acilacagini soyler
win.state(newstate="normal") # normal, zoomed(tam ekran), iconic(kucultulmus), withdrawn(gizli) newstate bu 4 parametreyi alabilir
win.mainloop() # tkinter uygulamasinin ana dongusunu baslatir ve uygulama bu dongu calistigi surece acik kalir
#win.mainloop() olmadan tkinter uygulamasi calismaz!