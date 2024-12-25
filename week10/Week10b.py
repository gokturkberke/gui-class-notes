# Install customtkinter: https://customtkinter.tomschimansky.com/
# Basic CTk GUI with classes

import customtkinter as ctk


class CTkApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Week 10")
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.lbl = ctk.CTkLabel(self, text="GUI Programming with Python", fg_color=("orange", "green"), corner_radius=20)
        self.btn = ctk.CTkButton(self, text="Change Appearance", command=self.change_appearance)

    def create_layout(self):
        self.lbl.pack(pady=20)
        self.btn.pack()

    def change_appearance(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")


app = CTkApp()
# Bu Sinif tabanli week10a fonksiyon tabanliydi;sinif tabanli olmasi daha duzenli, buyuk projeler icin ve kod tekrarini azaltan bir yontemdir.