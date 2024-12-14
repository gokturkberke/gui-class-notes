import tkinter as tk

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# side: Defines the side of the container where the widget is placed (top, left, right, bottom)
label1.pack(ipadx=10, ipady=10, fill="x", side="top") #ust kenara hizalar pencereyi buyutugumuzde(dikey) label2 ve label3un aksine genislemez cunku
#fill="y" parametresinin side="top" ile birlikte çalışmamasından kaynaklanır. Çünkü fill="y", side="top" ile kullanıldığında etkisizdir.
#side="top" ayarlandığında, fill yatayda (x ekseni) genişlemeyi sağlar; yani, fill="x" kullanıldığında label1 yatay olarak genişler, ancak dikeyde genişlemez.
#fill="y" sadece side="left" veya side="right" kullanıldığında dikey eksende etkili olur.
label2.pack(ipadx=10, ipady=10, fill="y", side="left") #pencerenin sol kenarina hizalar
label3.pack(ipadx=10, ipady=10, fill="y", side="right")

win.mainloop()
