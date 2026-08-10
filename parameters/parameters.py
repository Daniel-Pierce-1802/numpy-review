# Author: Daniel J. Pierce
# Date: 2026-08-10

import numpy as np
import matplotlib.pyplot as plt

# Define Constants
angles = np.deg2rad(np.array([15, 30, 45, 60, 75]))
v_0 = 15
g = 9.81


def main():
    plot_trajectory(angles)


def plot_trajectory(angles):
    """
    Takes as input a NumPy array of angles and creates a plot comparing the trajectories for all the angles provided as input.
    """
    fig, ax = plt.subplots()
    ax.set_xlabel("Position (horizontal component)")
    ax.set_ylabel("Position (vertical component)")
    ax.set_title("Horizontal position vs. Vertical position")

    for angle in angles:
        final_time = flight_time(angle)
        t = np.linspace(0, final_time, 100)
        x, y = trajectory(t, angle)
        ax.plot(x, y, label=f"{round(np.rad2deg(angle))}\N{DEGREE SIGN}")

    ax.legend()
    plt.show()


def flight_time(angle):
    """
    Takes as input an angle in radians and calculates the total flight time of a projectile
    """
    t = (2 * v_0 * np.sin(angle)) / g

    return t


def trajectory(time, angle):
    """
    Takes as input an array of times and the angle in radians. Calculates the horizontal and vertical components of position and returns them as two numpy arrays.
    """
    x = v_0 * np.cos(angle) * time
    y = v_0 * np.sin(angle) * time - 0.5 * g * time**2

    return x, y


if __name__ == "__main__":
    main()
