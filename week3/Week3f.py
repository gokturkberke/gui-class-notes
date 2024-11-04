import tkinter as tk
from tkinter import ttk

def button_handler(): #send butonunda calisir
    label1.configure(text=entry1.get() + " " + selected_combo_item.get() + " " + selected_radio_item.get())
#texti alir hangi option secenegini ve hangi dugmeye tikladiginin bilgisini alir
def checkbox_handler():
    if checkbox_state.get() == "Enabled": #enable button tikli oldugunda send yapabiliyoruz
        button1.configure(state="normal")
        label1.configure(text="Button enabled.")
    else:
        button1.configure(state="disabled") #enable buton disable oldugunda send butonu ozelligin kaybediyo
        label1.configure(text="Button disabled.")

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x330+100+100")
selected_combo_item = tk.StringVar(value="Option 2")
selected_radio_item = tk.StringVar()
checkbox_state = tk.StringVar(value="Enabled")

frame1 = ttk.LabelFrame(win, text="Some GUI Widgets") #fram1 bir etiket cercevesi olusturur;icersiinde diger bilesenleri barindiracak olan bir cerceve
label1 = ttk.Label(frame1, text="Label")
entry1 = ttk.Entry(frame1, width=30) #kullanicidan bir metin girisi alani olusturur genisligi 30 karakter olabilir
combo1 = ttk.Combobox(frame1, width=15, textvariable=selected_combo_item, state="readonly") #acilir menu olusturur(option1'in ustune tiklayinca acilan sey mantigi) 15 karakter olabilir max
combo1["values"] = ("Option 1", "Option 2")  #selected combo item ile baglanmis,state="readonly" ile kulalnici acilir menuden yalnizca secim yapabilir, metni duzenleyemez
radio1 = ttk.Radiobutton(frame1, text="Item 1", value="A", variable=selected_radio_item)  # command=callback_func
radio2 = ttk.Radiobutton(frame1, text="Item 2", value="B", variable=selected_radio_item)  #radyo dugmelerini olusturan kodlar
checkbox1 = ttk.Checkbutton(frame1, text="Enable button", onvalue="Enabled", offvalue="Disabled",
                            variable=checkbox_state, command=checkbox_handler) #onay kutusu kodu
button1 = ttk.Button(frame1, text="Send", command=button_handler)  # state="disabled" (normal, disabled, active)
#send butonunu olusturur button handler fonksiyonu calisir tiklandiginda
frame1.pack(fill="both", expand=True, padx=10, pady=10)
label1.pack(pady=10)
entry1.pack(pady=10) 
combo1.pack(pady=10) #tum bilesenler frame1 icinde duzenlenir,yukaridan asagiya dogru yerlestirilir
radio1.pack(pady=10)
radio2.pack(pady=10)
checkbox1.pack(pady=10)
button1.pack(pady=10)

win.mainloop()
