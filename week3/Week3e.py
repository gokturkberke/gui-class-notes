import tkinter as tk

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")

# uniform: Creates groups of rows or columns that will resize uniformly. It can take any string value of your choice.
win.columnconfigure(index=0, weight=1, uniform="eq") #uniform eq satir ve sutun gruplarinin ayni oranda genislemesini saglar
win.columnconfigure(index=1, weight=2, uniform="eq") #yani pencere genisletilirse hepsi ayni oranda genisler uniform koduyla
win.columnconfigure(index=2, weight=3, uniform="eq")
win.rowconfigure(index=0, weight=1, uniform="eq")#rowconfigure -> satir ozelliklerini ayarlamak icin
win.rowconfigure(index=1, weight=1, uniform="eq")
win.rowconfigure(index=2, weight=1, uniform="eq")
#weight ne kadar alan kaplayacagini belirtir
#satir olarak 3 label mesela ayni boyutta olur fakat sutun genisligi olarak en alttaki en buyuk olur gibi
label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# sticky: Controls widget alignment or stretching within the grid cell.
# rowspan / columnspan: Allows a widget to span multiple rows or columns.
label1.grid(row=0, column=0, sticky="nswe") # bulundugu hureye 4 yonde esneyerek genislemesini saglar(north,south,west,east) rowspan=2
label2.grid(row=1, column=2, sticky="nswe") #1. satir 2.sutunda yer alir
label3.grid(row=2, column=1, sticky="nswe") # columnspan=2

win.mainloop()
#rowspan bi widgetin kac satira yayilacagini belirler
#columnspan aynisinin sutunlusu
#sticky : bir widget'ın yerleştirildiği hücre içinde nasıl hizalanacağını belirtir