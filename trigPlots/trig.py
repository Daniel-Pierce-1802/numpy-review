#Author: Daniel J. Pierce
#Date: 2026-08-05

import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 4*np.pi, 100)

    first_func = np.sin(x)
    second_func = np.cos(x)
    third_func = np.sin(x) + np.cos(x)

    response = input("Would you like to plot sin, cos, the sum, or all functions (Enter sin, cos, sum, or all)?: ")

    if response == "sin":
        plot_function(x, first_func, "Sin(x)")
    elif response == "cos":
        plot_function(x, second_func, "Cos(x)")
    elif response == "sum":
        plot_function(x, third_func, "Sin(x) + Cos(x)")
    elif response == "all":
        plot_all_functions(x, first_func, second_func, third_func)
    else:
        print("Invalid selection.")

def plot_function(x, function, label = None):
    fig, ax = plt.subplots()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(fr"{label} from $0$ to $4\pi$")
    ax.plot(x, function, label = f"{label}")
    ax.legend()
    plt.show()

def plot_all_functions(x, first_func, second_func, third_func):
    fig, ax = plt.subplots()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(r"All functions from $0$ to $4\pi$")
    ax.plot(x, first_func, label = "Sin(x)")
    ax.plot(x, second_func, label = "Cos(x)")
    ax.plot(x, third_func, label = "Sin(x) + Cos(x)")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()