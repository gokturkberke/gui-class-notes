# Install customtkinter: https://customtkinter.tomschimansky.com/
# Scrollable frame

import customtkinter as ctk


class CTkApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x450")
        self.title("Week 10")
        self.labels = []
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.frame1 = ctk.CTkScrollableFrame(self, label_text="List of Labels")
        self.btn1 = ctk.CTkButton(self.frame1, text="Add labels", command=self.add_labels)
        self.btn2 = ctk.CTkButton(self.frame1, text="Remove labels", command=self.remove_labels)

    def create_layout(self):
        self.frame1.pack(pady=20, padx=20, fill="both", expand=True)
        self.btn1.pack(pady=(10, 0))
        self.btn2.pack(pady=(10, 0))

    def add_labels(self):
        list_size = len(self.labels)
        for i in range(20):
            self.labels.append(ctk.CTkLabel(self.frame1, text=f"Label {list_size + i + 1}"))
            self.labels[list_size+i].pack(pady=(10, 0))

        self.frame1.configure(label_text=f"List of Labels ({len(self.labels)})")

    def remove_labels(self):
        for l in self.labels:
            l.destroy()
        self.labels.clear()
        self.frame1.configure(label_text="List of Labels")


app = CTkApp()
