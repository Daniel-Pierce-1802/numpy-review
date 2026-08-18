# Author: Daniel J. Pierce
# Date: 2026-08-17

import matplotlib.pyplot as plt
import numpy as np 


# Solving dy/dt = -ky


def main():
    # Define initial conditions

    y0 = 10
    k = 0.5
    h = 0.1

    # Initialize arrays for plotting

    t_numerical, y_numerical = [], []
    t = 0.0

    # Euler's Method
    y_old = y0

    while t < 1.0:
        y = y_old + h * -k * y_old
        y_old = y
        t += h
        print(y_old)


    
    



if __name__ == "__main__":
    main()