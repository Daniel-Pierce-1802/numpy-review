#Author: Daniel J. Pierce
#Date: 2026-08-03

import numpy as np 

def main():

    #Define starting variables
    t = np.linspace(0, 10)
    x_initial = 0
    v_initial = 15
    acceleration = 6

    #Calculate Position and Velocity at each time
    position = calculate_position(x_initial, v_initial, acceleration, t)
    velocity = calculate_velocity(v_initial, acceleration, t)

    for value, time in zip(position, t):
        print(f"Time = {time} s, Position = {value} m")
    
    for value, time in zip(velocity, t):
        print(f"Time = {time} s, Velocity = {value} m/s")
    
    #Find maximum position
    print(f"Maximum Position = {np.max(position)} m")

    #Find time nearest maximum position
    maximum_index = np.argmax(position)
    print(f"Maximum Position occurs at time = {t[maximum_index]} s")

    #Find first time position becomes negative

    boolean_array = position < 0
    negative_position_indices = np.where(boolean_array)[0]
    if len(negative_position_indices) == 0:
        print("The position remains positive throughout the entire motion of the object")
    else:
        minimum_index = np.min(negative_position_indices)
        print(f"Position becomes negative at {t[minimum_index]} s")


def calculate_position(x_initial, v_initial, a, t):
    x = x_initial + v_initial * t + 0.5 * a * t**2
    return x

def calculate_velocity(v_initial, a, t):
    v = v_initial + a * t
    return v

if __name__ == "__main__":
    main()