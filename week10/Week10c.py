# Install customtkinter: https://customtkinter.tomschimansky.com/
# Common CTk widgets

import customtkinter as ctk


class CTkApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x450")
        self.title("Week 10")
        self.rb_value = ctk.IntVar(value=1)
        self.current_appearance = ctk.StringVar(value="Light")
        ctk.set_appearance_mode(self.current_appearance.get())
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.frame1 = ctk.CTkFrame(self)
        self.lbl1 = ctk.CTkLabel(self.frame1, text="Label")
        self.entry1 = ctk.CTkEntry(self.frame1, placeholder_text="Type your message.")
        self.combo1 = ctk.CTkComboBox(self.frame1, values=["Item 1", "Item 2", "Item 3"])
        self.opt_menu1 = ctk.CTkOptionMenu(self.frame1, values=["Item 1", "Item 2", "Item 3"])
        self.chk1 = ctk.CTkCheckBox(self.frame1, text="Checkbox", onvalue="checked", offvalue="unchecked")
        self.radio1 = ctk.CTkRadioButton(self.frame1, text="Item 1", variable=self.rb_value, value=1)
        self.radio2 = ctk.CTkRadioButton(self.frame1, text="Item 2", variable=self.rb_value, value=2)
        self.btn1 = ctk.CTkButton(self.frame1, text="Button", command=self.button_click)
        self.progress1 = ctk.CTkProgressBar(self.frame1)
        self.slider1 = ctk.CTkSlider(self.frame1, from_=0, to=1, command=self.get_slider_value)
        self.switch1 = ctk.CTkSwitch(self.frame1, textvariable=self.current_appearance, command=self.change_appearance)

        self.progress1.set(0.8)
        self.slider1.set(0.8)

        self.entry1.bind("<KeyRelease>", self.set_text) #kullanici entry alanina bir sey yazdiginda set_text fonksiyonunu cagirir

    def create_layout(self):
        self.frame1.pack(pady=20, padx=20, fill="both", expand=True)
        self.lbl1.pack(pady=(10, 0))
        self.entry1.pack(pady=(10, 0))
        self.combo1.pack(pady=(10, 0))
        self.opt_menu1.pack(pady=(10, 0))
        self.chk1.pack(pady=(10, 0))
        self.radio1.pack(pady=(10, 0))
        self.radio2.pack(pady=(10, 0))
        self.btn1.pack(pady=(10, 0))
        self.progress1.pack(pady=(10, 0))
        self.slider1.pack(pady=(10, 0))
        self.switch1.pack(pady=(10, 0))

    def set_text(self, event):
        self.lbl1.configure(text=self.entry1.get())

    def button_click(self):
        self.lbl1.configure(text=f"Combobox value is {self.combo1.get()}.\n"
                                 f"Option menu value is {self.opt_menu1.get()}.\n"
                                 f"Checkbox is {self.chk1.get()}.\n"
                                 f"Radio button value is {self.rb_value.get()}.")
        print(self.rb_value.get())

    def get_slider_value(self, value):
        self.progress1.set(value)
        self.lbl1.configure(text=f"Slider value: {value}")

    def change_appearance(self):
        if self.current_appearance.get() == "Dark":
            self.current_appearance.set("Light")
        else:
            self.current_appearance.set("Dark")

        ctk.set_appearance_mode(self.current_appearance.get())


app = CTkApp()