#Author: Daniel J. Pierce
#Date: 2026-08-03

import numpy as np

def main():
    a = np.array([2, -1, 3])
    b = np.array([4, 0, -2])

    #Calculate vector sum
    print(add_vector(a,b))

    #Calculate vector difference
    print(subtract_vector(a,b))

    #Calculate scaled vector
    print(scale_vector(3, a))

    #Calculate dot product
    print(dot_product(a,b))

    #Calculate the magnitude
    print(f"Magnitude of vector a: {magnitude(a)}\nMagnitude of vector b: {magnitude(b)}")

    #Calculate the angle between the two vectors (in degrees)
    print(f"Angle: {find_angle(a,b)}")

def add_vector(a,b):
    return a + b

def subtract_vector(a,b):
    return a - b

def scale_vector(scalar, vector):
    return scalar * vector

def dot_product(a,b):
    return np.dot(a,b)

def magnitude(a):
    return np.linalg.norm(a, ord = 2)

def find_angle(a,b):
    return (np.arccos((dot_product(a,b))/(magnitude(a) * magnitude(b)))) * (180/np.pi)

if __name__ == "__main__":
    main()