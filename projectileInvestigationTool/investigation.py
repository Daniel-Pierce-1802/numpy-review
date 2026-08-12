# Author: Daniel J. Pierce
# Date: 2026-08-11

import numpy as np
import matplotlib.pyplot as plt


def main():
    v0, launch_angle, y0, g = get_constants()
    radian_angle = np.deg2rad(launch_angle)
    time_final = flight_time(radian_angle, v0, g)
    time = np.linspace(0, time_final, 100)

    # Print time of flight
    print(f"The total time of flight is {time_final} s")

    # Find trajectory
    x, y = trajectory(time, radian_angle, v0, g, y0)
    position = (x, y)

    # Save Trajectory Data
    

    # Find Vertical Velocity
    velocity = calculate_velocity(v0, g, time)

    # Print range (based on available sample points)
    print(f"The total range is {np.max(x)} m")

    # Print Max height (based on available sample points)
    print(f"The maximum height is {np.max(y)} m")

    # Plot Position vs. Time
    plot_values(
        time,
        position,
        xlabel="Time (s)",
        ylabel="Position (m)",
        title="Position vs. Time",
        labels=["Position (x-component)", "Position (y-component)"],
        save="Position_vs_time.png",
    )

    # Plot vertical velocity vs. Time
    plot_values(
        time,
        [velocity],
        "Time (s)",
        "Velocity (m/s)",
        "Velocity vs. Time",
        ["Vertical Velocity"],
        "velocity_vs_time.png",
    )

    # Plot Trajectory
    plot_values(
        x,
        [y],
        "Position (x-component)",
        "Position (y-component)",
        "Trajectory",
        ["Trajectory"],
        "trajectory.png",
    )


def get_constants():
    while True:
        try:
            v0 = float(input("Enter initial velocity: "))
            launch_angle = float(input("Enter launch angle: "))
            y0 = float(input("Enter initial height: "))
            g = float(input("Enter gravitational acceleration: "))
            break
        except ValueError:
            print("Invalid value(s). Please try again.")

    return v0, launch_angle, y0, g


def flight_time(angle, v_0, g):
    """
    Takes as input an angle in radians and calculates the total flight time of a projectile
    """
    t = (2 * v_0 * np.sin(angle)) / g

    return t


def trajectory(time, angle, v_0, g, y0):
    """
    Takes as input an array of times and the angle in radians. Calculates the horizontal and vertical components of position and returns them as two numpy arrays.
    """
    x = v_0 * np.cos(angle) * time
    y = y0 + v_0 * np.sin(angle) * time - 0.5 * g * time**2

    return x, y


def plot_values(x, y, xlabel, ylabel, title, labels, save):
    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    for value, label in zip(y, labels):
        ax.plot(x, value, label=label)

    ax.legend()
    plt.savefig(save)
    plt.show()


def calculate_velocity(v_initial, a, t):
    v = v_initial + a * t
    return v


if __name__ == "__main__":
    main()
