# Author: Daniel J. Pierce
# Date: 2026-08-13

import numpy as np

def main():
    # Define x
    x = 2

    analytical_solution = 3*x**2

    # Calculate numerical derivative
    f_prime_vals, h_vals = numerical_derivative(x)
    for f_prime, h in zip(f_prime_vals, h_vals):
        absolute_error = error(f_prime, analytical_solution)
        print(f"h = {h}, f_prime = {f_prime}, absolute error = {absolute_error}")

    # Print actual value
    print(f"The analytical value is: {analytical_solution}")

def numerical_derivative(x):
    h_vals = np.logspace(0, -16, 17)

    f_prime_values = []
    
    # Define f'
    for h in h_vals:
        f_prime = ((x + h)**3 - (x - h)**3)/(2*h)
        f_prime_values.append(f_prime)
    
    return f_prime_values, h_vals

def error(numerical, exact):
    
    return np.abs(numerical - exact)



if __name__ == "__main__":
    main()