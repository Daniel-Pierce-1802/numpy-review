# Author: Daniel J. Pierce
# Date: 2026-08-17

import matplotlib.pyplot as plt
import numpy as np

# Solving dy/dt = -ky


def main():
    # Define initial conditions

    y0 = 10.0
    k = 0.5

    # Initialize arrays for plotting

    t_analytical = np.linspace(0, 1, 100)
    y_analytical = y0 * np.exp(-k * t_analytical)

    # Euler's Method for multiple timesteps & plot against analytical solution

    time_steps = np.logspace(0, -5, 6)

    fig, ax = plt.subplots()
    ax.set_title(r"Numerical Solution to $dy/dt = -ky$")
    ax.set_xlabel("Time")
    ax.set_ylabel("y")

    for dt in time_steps:
        t_numerical, y_numerical = eulers_method(y0, k, dt)
        ax.plot(t_numerical, y_numerical, label=f"Euler's Method (dt = {dt})")
    
    ax.plot(t_analytical, y_analytical, label="Analytical Solution", linestyle = "--", linewidth = 2.5)
    ax.legend()
    plt.show()


def eulers_method(y0, k, dt):

    t_numerical, y_numerical = [0.0], [y0]
    t = 0.0
    y_current = y0

    while t < 1.0:
        y_next = y_current + dt * (-k * y_current)
        y_current = y_next
        y_numerical.append(y_current)
        t += dt
        t_numerical.append(t)

    return t_numerical, y_numerical


if __name__ == "__main__":
    main()
