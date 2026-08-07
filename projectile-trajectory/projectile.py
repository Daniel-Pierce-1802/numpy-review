# Author: Daniel J. Pierce
# Date: 2026-08-07

import numpy as np
import matplotlib.pyplot as plt

# Define constants
g = 9.8
v_0 = 15


def main():
    launch_angle_degrees = float(input("Enter a launch angle in degrees: "))

    # Convert angle to radians
    launch_angle = np.deg2rad(launch_angle_degrees)

    # Calculate flight time
    time_final = flight_time(launch_angle)
    print(f"The total time of flight is: {time_final} s")

    # Create array of times
    time = np.linspace(0, time_final, 100)

    # Calculate trajectory
    x, y = trajectory(time, launch_angle)

    # Generate Plot
    projectile_plot(x, y)

    # Find approximate max height (based on available sample values)
    print(f"The maximum height is: {np.max(y)} m")

    # Find approximate horizontal range (based on available sample values)
    print(f"The horizontal range is: {np.max(x)} m")


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


def projectile_plot(x, y):
    """
    Takes as input two arrays for horizonal and vertical position components and plots them against each other.
    """
    fig, ax = plt.subplots()
    ax.set_xlabel("Position (horizontal component)")
    ax.set_ylabel("Position (vertical component)")
    ax.set_title("Horizontal position vs. Vertical position")
    ax.plot(x, y, label="x vs. y")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
