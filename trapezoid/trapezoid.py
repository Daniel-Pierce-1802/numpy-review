# Author: Daniel J. Pierce
# Date: 2026-08-13

import numpy as np

def main():
    # My approximation
    integral_approximation, error = trapezoidal_rule(0, np.pi, 20)
    print(f"My approximation = {integral_approximation}, Error = {error}%")

    #NumPy approximation
    x = np.linspace(0, np.pi, 21)
    y = np.sin(x)
    print(f"NumPy approximation = {np.trapezoid(y, x = x)}")



def trapezoidal_rule(a, b, n):
    delta_x = (b - a)/n
    x = np.arange(a, b, delta_x)
    running_sum = 0
    for value in x:
        integral_approximation = ((np.sin(value) + np.sin(value + delta_x))/2) * delta_x
        running_sum = running_sum + integral_approximation
    
    error = (np.abs(running_sum - 2)/2) * 100

    return running_sum, error




if __name__ == "__main__":
    main()