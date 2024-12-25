# Install customtkinter: https://customtkinter.tomschimansky.com/
# Textbox, segmented button, and tab view widgets

import customtkinter as ctk


class CTkApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x450")
        self.title("Week 10")
        self.sb_value = ctk.StringVar(value="Option 3")
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.frame1 = ctk.CTkFrame(self)
        self.textbox1 = ctk.CTkTextbox(self.frame1, wrap="none", width=240, height=80)
        self.segmented_btn1 = ctk.CTkSegmentedButton(self.frame1, values=["Option 1", "Option 2", "Option 3"], variable=self.sb_value, command=self.sb_selection)
        self.tabview1 = ctk.CTkTabview(self.frame1, anchor="sw")  # anchor sets the placement of the segmented tab buttons.
        self.tab1 = self.tabview1.add("Tab 1")
        self.tab2 = self.tabview1.add("Tab 2")
        self.tabview1.set("Tab 2") #baslangicta acik olacak sekme tab2 olarak belirlendi.
        self.lbl1 = ctk.CTkLabel(self.tab1, text="This is tab 1.")
        self.lbl2 = ctk.CTkLabel(self.tab2, text="This is tab 2.")
        self.btn1 = ctk.CTkButton(self.tab2, text="Exit", command=lambda : self.destroy())

    def create_layout(self):
        self.frame1.pack(pady=20, padx=20, fill="both", expand=True)
        self.textbox1.pack(pady=(10, 0))
        self.segmented_btn1.pack(pady=(10, 0))
        self.tabview1.pack(padx=10, pady=10)
        self.lbl1.pack(pady=(30, 0))
        self.lbl2.pack(pady=(30, 0))
        self.btn1.pack(pady=(30, 0))

    def sb_selection(self, value):
        self.textbox1.insert("end", f"{value} selected.\n")
        self.textbox1.see("end")


app = CTkApp()