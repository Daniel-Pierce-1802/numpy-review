# Author: Daniel J. Pierce
# Date: 2026-08-19
"""
Description: This project solves the differential equation for radioactive decay, dN/dt = -λ * N, by using Euler's Method and RK4. It then plots the numerical results against
the analytical solution for comparison.
"""

import numpy as np 
import matplotlib.pyplot as plt 

def main():
    euler_N, euler_t = euler(0.01, 0.001, 1000)

    # Plot solutions
    fig, ax = plt.subplots()
    ax.set_title("Comparison of Numerical Methods for Radioactive Decay")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("N")
    ax.plot(euler_t, euler_N, label = "Euler's Method")
    ax.legend()
    plt.show()

def euler(λ, dt, N_0):
    N_numerical, t_numerical = [N_0], [0.0]
    N_current = N_0
    t = 0.0
    while t < 1000.0:
        N_next = N_current + dt * (-λ * N_current)
        N_current = N_next
        N_numerical.append(N_current)
        t += dt
        t_numerical.append(t)
    
    return N_numerical, t_numerical

def RK4():
    ...




if __name__ == "__main__":
    main()