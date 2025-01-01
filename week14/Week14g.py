# Install matplotlib: https://matplotlib.org/stable/
# Histogram

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1, size=1000)
#loc 0 specifies the mean of the distribution
#scale=1 specifies the standard deviation of the distribution
#size 1000 specifies the number of random numbers to generate

fig, ax = plt.subplots()
ax.hist(data, bins=30)# 'bins=30' histogramda kaç aralıklı kutucuk olduğunu belirtir

ax.set_title("Histogram")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")

plt.show()
