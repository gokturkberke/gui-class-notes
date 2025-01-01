# Install matplotlib: https://matplotlib.org/stable/
# Scatter plot, custom colors and sizes

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]
sizes = [50, 100, 200, 300, 400]
colors = ["red", "green", "blue", "orange", "lime"]

fig, ax = plt.subplots() # Bir figure (grafik alanı) ve bir axes (çizim yapılacak alan) oluşturuluyor
ax.scatter(x_values, y_values, s=sizes, c=colors)

ax.set_title("Colored Scatter Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

plt.show()
