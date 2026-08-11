# Author: Daniel J. Pierce
# Date: 2026-08-11

import numpy as np 
import matplotlib.pyplot as plt 

def main():
    v0, launch_angle, y0, g = get_constants()
    radian_angle = np.deg2rad(launch_angle)
    time = flight_time(radian_angle, v0, g)

    #Print time of flight
    print(f"The total time of flight is {time} s")


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


if __name__ == "__main__":
    main()