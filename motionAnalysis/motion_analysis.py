# Author: Daniel J. Pierce
# Date: 2026-08-04

import numpy as np


def main():
    data = np.loadtxt("motion_data.txt", skiprows=1)
    time = data[:, 0]
    position = data[:, 1]

    # Calculate Average Position
    print(f"Average Position: {np.mean(position)}")

    # Calculate Minimum Position
    print(f"Minimum Position: {np.min(position)}")

    # Calculate Maximum Position
    print(f"Maximum Position: {np.max(position)}")

    # Calculate Range of Position
    print(f"Range of Position: {np.ptp(position)}")

    # Calculate Midpoint time
    midpoint_time = (time[1:] + time[:-1]) / 2

    # Estimate Velocity with finite differences
    velocity = finite_difference(position, time)
    for time_val, velocity_val in zip(midpoint_time, velocity):
        print(f"At time = {time_val:.2f} s, velocity = {velocity_val:.2f} m/s")

    # Identify largest speed
    speed = np.abs(velocity)
    print(
        f"The maximum speed is: {np.max(speed)} m/s and occurs at {midpoint_time[np.argmax(speed)]} s"
    )

    # Save Velocity Data and corresponding midpoint time
    new_data = np.column_stack((midpoint_time, velocity))
    print(save_data(new_data))


def finite_difference(position, time):
    velocity = np.diff(position) / np.diff(time)

    return velocity


def save_data(data):
    np.savetxt(
        "velocity_data.txt",
        data,
        fmt="%.2f",
        header="Midpoint Time\tVelocity Data (m/s)",
    )

    return f"Data saved successfully!"


if __name__ == "__main__":
    main()
