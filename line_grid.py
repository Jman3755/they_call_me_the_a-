import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 50, 100, 150, 200])
y = np.array([0, 50, 100, 150, 200])


plt.plot(x, y)
plt.title("Sample Plot with Grid")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.grid(True) # Adds grid lines
plt.show()

