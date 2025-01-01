# Install matplotlib: https://matplotlib.org/stable/
# Bar plot

import matplotlib.pyplot as plt

x_values = ["A", "B", "C", "D"]
y_values = [5, 7, 6, 8]

fig, ax = plt.subplots()

# Bar plot (çubuk grafik) çiziliyo
ax.bar(x_values, y_values)

ax.set_title("Bar Plot")
ax.set_xlabel("Letters")
ax.set_ylabel("Numbers")

plt.show()
