# Install matplotlib: https://matplotlib.org/stable/
# Simple plot

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4]
y_values = [5, 7, 6, 8]

plt.plot(x_values, y_values)

# For explicit Figure and Axes manipulation:
# fig, ax = plt.subplots() # Create a Figure with one Axes
# ax.plot(x_values, y_values)
#bir cizgi grafigi cizer ve noktalari birlestirir 1 ile 5 i 2 ile 7yi ...
plt.show()
