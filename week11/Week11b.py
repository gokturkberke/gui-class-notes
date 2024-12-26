# Install ttkbootstrap: https://ttkbootstrap.readthedocs.io/en/latest/
# Basic ttkbootstrap GUI with classes

import ttkbootstrap as ttk


class GUIApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.geometry("500x500")
        self.title("Week 11")
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.btn1 = ttk.Button(self, text="Button 1", bootstyle="success")
        self.btn2 = ttk.Button(self, text="Button 2", bootstyle=("info", "outline"))
        self.cbtn1 = ttk.Checkbutton(self, text="Check button", bootstyle="warning-round-toggle")
        self.date_entry = ttk.DateEntry(self, bootstyle="success", width=10)

    def create_layout(self):
        self.btn1.pack(padx=15, pady=(30, 15))
        self.btn2.pack(padx=15, pady=15)
        self.cbtn1.pack(padx=15, pady=15)
        self.date_entry.pack(padx=15, pady=15)


app = GUIApp()
