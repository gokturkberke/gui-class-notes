import tkinter as tk
from tkinter import ttk

# Conversion function
def convert(): #deger donusturme fonksiyonu
    try:
        value = float(entry.get())
        if unit_combobox.get() == "Miles to Kilometers": #unit.combobox.get() fonksiyonu ile kullanici miles to kilometerrs veya kilometer to miles biirmlerinden birini secer
            result = value * 1.60934
            result_label.configure(text=f"{result:.2f} Kilometers")
            #.2f formati result değeri 5.6789 ise, text=f"{result:.2f}" ifadesi 5.68 olarak gösterilir
            #yani sayinin 2 ondalik basamagina kadar gosterir
        elif unit_combobox.get() == "Kilometers to Miles":
            result = value / 1.60934
            result_label.configure(text=f"{result:.2f} Miles")
    except ValueError: #sayi degilse entryden alinan giris
        result_label.configure(text="Invalid input. Please enter a number.")

# Main window
win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")
win.resizable(False, False)

# LabelFrame to contain all widgets
container = ttk.LabelFrame(win, text="Unit Converter", padding="10") #cerceve ekledik
#padding de cerceve icine kenar boslugu ekler
container.pack(padx=15, pady=15, fill="both", expand=True)

# Configure grid rows and columns
container.columnconfigure(index=0, weight=1)
container.columnconfigure(index=1, weight=2)
container.rowconfigure(index=0, weight=1)
container.rowconfigure(index=1, weight=1)
container.rowconfigure(index=2, weight=1)
container.rowconfigure(index=3, weight=1)

# Label and Entry for input
entry_label = ttk.Label(container, text="Enter Value:")
entry_label.grid(row=0, column=0, padx=5, pady=5)
entry = ttk.Entry(container)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="we") #kullanicinin girecegi degeri
#0.satir 1. sutuna yerlestirilir ve yatay yonde (west-east) genisletir

# Combobox for unit selection
combo_label = ttk.Label(container, text="Convert:")
combo_label.grid(row=1, column=0, padx=5, pady=5)
unit_combobox = ttk.Combobox(container, values=["Miles to Kilometers", "Kilometers to Miles"], state="readonly") #readonly menuden secim yapabilir manuel giris yapilamaz
unit_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="we")
unit_combobox.set("Miles to Kilometers")  # Default value (otomatik olarak ayarlama baslangic icin)

# Convert button
convert_button = ttk.Button(container, text="Convert", command=convert) #convert butonunu tetikliyor
convert_button.grid(row=2, column=1, padx=5, pady=5, sticky="e") #butonu saga hizalar

# Label to display the result
result_label = ttk.Label(container, text="")
result_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2) #columnspan sonucun her iki stuunun da kaplamasini saglar

# Main loop
win.mainloop()
