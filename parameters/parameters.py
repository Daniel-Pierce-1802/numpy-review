# Author: Daniel J. Pierce
# Date: 2026-08-10

import numpy as np
import matplotlib.pyplot as plt

def main():
    angles = np.deg2rad(np.array([15, 30, 45, 60, 75]))

    for angle in angles:
        plot_trajectory(angle)


def plot_trajectory(angle):
    ...



if __name__ == "__main__":
    main()