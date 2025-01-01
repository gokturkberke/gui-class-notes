# Install matplotlib: https://matplotlib.org/stable/
# Two plots with some customizations

import matplotlib.pyplot as plt

x1_values = [0, 2, 3, 4]
y1_values = [0, 1, 2, 4]
x2_values = [0, 1, 4, 6]
y2_values = [0, 1, 2, 1]

fig, ax = plt.subplots()

ax.set_xlim(0, 6) #X ekseni sinirlari belirleniyo
ax.set_ylim(0, 6) #Y ekseni sinirlari

# Grid  görünür hale getiriliyor, çizgi stili ":" (noktalı çizgi) olarak ayarlanıyor
ax.grid(visible=True, linestyle=":") # Some line styles: '-', '--', '-.', ':',

# Birinci grafik çiziliyor: Kırmızı renkli ve kesikli çizgi (linestyle="--")
ax.plot(x1_values, y1_values, linestyle="--", color="red")
ax.plot(x2_values, y2_values, color="green") 

# Grafik penceresinin başlığı ayarlanıyor
fig.canvas.manager.set_window_title("Sample Figure")

plt.show() # Grafiği ekranda gösteriyor
