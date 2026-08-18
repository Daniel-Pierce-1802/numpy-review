# Author: Daniel J. Pierce
# Date: 2026-08-17

import matplotlib.pyplot as plt
import numpy as np 


# Solving dy/dt = -ky


def main():
    # Define initial conditions

    y0 = 10.0
    k = 0.5
    dt = 0.1

    # Initialize arrays for plotting

    t_numerical, y_numerical = [0.0], [y0]
    t_analytical = np.linspace(0, 1, 100)
    y_analytical = y0 * np.exp(-k * t_analytical)

    # Euler's Method
    t = 0.0
    y_current = y0

    while t < 1.0:
        y_next = y_current + dt * (-k * y_current)
        y_current = y_next
        y_numerical.append(y_current)
        t += dt
        t_numerical.append(t)

    # Plot Euler's Method against analytical solution
    fig, ax = plt.subplots()
    ax.set_title(r"Numerical Solution to $dy/dt = -ky$")
    ax.set_xlabel("Time")
    ax.set_ylabel("y")
    ax.plot(t_numerical, y_numerical, label = "Euler's Method")
    ax.plot(t_analytical, y_analytical, label = "Analytical Solution")
    ax.legend()
    plt.show()
    
    



if __name__ == "__main__":
    main()