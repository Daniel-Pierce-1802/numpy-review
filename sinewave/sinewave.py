#Author: Daniel J. Pierce
#Date: 2026-08-05

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi)

y = np.sin(x)

#Create Plot

fig, ax = plt.subplots()
ax.plot(x, y, label = "sin(x)")
ax.axhline(y=0, label = "y = 0", color = "Red")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Sine Function from $0$ to $4\pi$")
ax.grid()
ax.legend()

plt.show()


