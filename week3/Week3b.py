import tkinter as tk

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# fill: Controls whether the widget should expand to fill the space allocated to it in the specified direction(s).
# expand: Controls whether the widget should be given extra space if the parent widget has any extra space available.
# anchor: Defines how the widget is positioned within its packing area (n, s, w, e, ne, ...).
label1.pack(ipadx=10, ipady=10, fill="y", expand=True)  # fill: none, x, y, both
label2.pack(ipadx=10, ipady=10, anchor="w") #anchor etiketi hangi yone yerlesecegini belirler burda w(west)
label3.pack(ipadx=10, ipady=10, anchor="e") #bu da sag kenara hizalar
#ipadx ve ipady etiketin genisligi(x) ve yuksekligine(y) 10 px yapar
#fill ="y" etiketin dikey olarak pencerenin tamamini doldurmasini saglar
#expand ise ana pencereyi buyuttukce label1 etiketimizi de ayni derecede uzatmayi saglar
win.mainloop()
