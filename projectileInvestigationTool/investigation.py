# Author: Daniel J. Pierce
# Date: 2026-08-11

import numpy as np 
import matplotlib.pyplot as plt 

def main():
    v0, launch_angle, y0, g = get_constants()


def get_constants():
    while True:
        try:
            v0 = float(input("Enter initial velocity: "))
            launch_angle = float(input("Enter launch angle: "))
            y0 = float(input("Enter initial height: "))
            g = float(input("Enter gravitational acceleration: "))
            break
        except ValueError:
            print("Invalid value. Please try again.")

    return v0, launch_angle, y0, g


if __name__ == "__main__":
    main()