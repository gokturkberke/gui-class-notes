# Center window

import tkinter as tk
from window_utils import center_window #bu fonksiyon pencerelerin ekranino rtasinda acilmasini saglar

# Create the main window
win = tk.Tk()

# Get the screen width and height
screen_width = win.winfo_screenwidth() #ekranin genisligini ve yukseklik bilgilerini alir
screen_height = win.winfo_screenheight()

# Define the desired window size
window_width = 400
window_height = 300

# Place the window using the "center_window" function
win.geometry(center_window(screen_width, screen_height, window_width, window_height))
#bilgiler kullanilarak pencerenin ekranin tam orasinda acilmasi saglanir
# Set the window title and icon
win.title("Week 5")
win.iconbitmap("python.ico")

win.mainloop()
#Bu kodun amacı, 400x300 piksel boyutlarında bir pencereyi ekranın tam ortasında açmak. Yani, ekranın genişliği ve yüksekliği göz önünde bulundurularak pencere düzgün bir şekilde yerleştirilir.