# Install customtkinter: https://customtkinter.tomschimansky.com/
# Unit converter

import customtkinter as ctk


class UnitConverter(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("blue")  # "blue" (standard), "green", "dark-blue"
        ctk.set_appearance_mode("light")
        self.geometry("310x200")
        self.title("Unit Converter")
        self.resizable(False, False)
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.container = ctk.CTkFrame(self)
        self.entry_label = ctk.CTkLabel(self.container, text="Enter Value:")
        self.entry = ctk.CTkEntry(self.container)
        self.combo_label = ctk.CTkLabel(self.container, text="Convert:")
        self.unit_combobox = ctk.CTkOptionMenu(self.container, values=["Miles to Kilometers", "Kilometers to Miles"])
        self.convert_button = ctk.CTkButton(self.container, text="Convert", width=80, command=self.convert)
        self.result_label = ctk.CTkLabel(self.container, text="Enter a number and click the Convert button.")

        self.bind("<Return>", lambda e : self.convert())

    def create_layout(self):
        self.container.pack(pady=10, padx=10, fill="both", expand=True)

        self.container.columnconfigure(index=0, weight=1)
        self.container.columnconfigure(index=1, weight=2)
        self.container.rowconfigure(index=0, weight=1)
        self.container.rowconfigure(index=1, weight=1)
        self.container.rowconfigure(index=2, weight=1)
        self.container.rowconfigure(index=3, weight=1)

        self.entry_label.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.entry.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="we")
        self.combo_label.grid(row=1, column=0, padx=10, pady=(10, 0))
        self.unit_combobox.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="we")
        self.convert_button.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="e")
        self.result_label.grid(row=3, column=0, padx=10, pady=(10, 0), columnspan=2)

    def convert(self):
        try:
            value = float(self.entry.get())
            if self.unit_combobox.get() == "Miles to Kilometers":
                result = value * 1.60934
                self.result_label.configure(text=f"{result:.2f} Kilometers")
            elif self.unit_combobox.get() == "Kilometers to Miles":
                result = value / 1.60934
                self.result_label.configure(text=f"{result:.2f} Miles")
        except ValueError:
            self.result_label.configure(text="Invalid input. Please enter a number.")


app = UnitConverter()