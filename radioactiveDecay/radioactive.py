# Author: Daniel J. Pierce
# Date: 2026-08-19
"""
Description: This project solves the differential equation for radioactive decay, dN/dt = -λ * N, by using Euler's Method and RK4. It then plots the numerical results against
the analytical solution for comparison.
"""

import numpy as np 
import matplotlib.pyplot as plt 

def main():
    euler_N, euler_t = euler(0.01, 10, 1000)
    rk4_t, rk4_N = RK4(1000, 10)

    # Compute analytical solution for plotting
    N_0 = 1000
    λ = 0.01
    t = np.linspace(0,100)
    analytical_solution = N_0 * np.exp(-λ*t)

    # Calculate error for each
    euler_error, rk4_error = calculate_error(euler_N, rk4_N, euler_t, rk4_t)
    print(f"Maximum error for Euler: {np.max(euler_error)}")
    print(f"Maximum error for RK4: {np.max(rk4_error)}")

    # Plot solutions
    fig, ax = plt.subplots()
    ax.set_title("Comparison of Numerical Methods for Radioactive Decay")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("N")
    ax.plot(euler_t, euler_N, label = "Euler's Method")
    ax.plot(rk4_t, rk4_N, label = "RK4")
    ax.plot(t, analytical_solution, label = "Analytical Solution", linestyle = "--")
    ax.legend()
    plt.show()

def euler(λ, dt, N_0):
    N_numerical, t_numerical = [N_0], [0.0]
    N_current = N_0
    t = 0.0
    while t < 100.0:
        N_next = N_current + dt * (-λ * N_current)
        N_current = N_next
        N_numerical.append(N_current)
        t += dt
        t_numerical.append(t)
    
    return np.array(N_numerical), np.array(t_numerical)

def RK4(N_current, dt):
    # Set Initial Conditions
    t = 0.0
    N_numerical, t_numerical = [N_current], [0.0]

    while t < 100.0:
        k1 = fun(t, N_current)
        k2 = fun(t + dt/2, N_current + (dt/2)*k1)
        k3 = fun(t + dt/2, N_current + (dt/2)*k2)
        k4 = fun(t + dt, N_current + (dt*k3))
        N_next = N_current + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
        N_numerical.append(N_next)
        N_current = N_next
        t += dt
        t_numerical.append(t)
    
    return np.array(t_numerical), np.array(N_numerical)

def fun(t, N_current):
    λ = 0.01
    fun = -λ * N_current

    return fun

def analytical_function(λ, N_0, t):
    return N_0 * np.exp(-λ * t)


def calculate_error(E_numerical, R_numerical, euler_time, rk4_time):
    analytical_euler = analytical_function(0.01, 1000, euler_time)
    analytical_rk4 = analytical_function(0.01, 1000, rk4_time)
    euler_error = np.abs(E_numerical - analytical_euler)
    rk4_error = np.abs(R_numerical - analytical_rk4)

    return euler_error, rk4_error





if __name__ == "__main__":
    main()