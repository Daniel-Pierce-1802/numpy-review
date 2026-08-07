#Author: Daniel J. Pierce
#Date: 2026-08-03

import numpy as np

#Create celsius values from -40 to 100 in steps of 5

celsius = np.arange(-40, 101, 5, dtype= float)

#Convert to Fahrenheit

fahrenheit = ((9/5) * celsius) + 32

#Print table

print("Celsius\tFahrenheit")

for celsius_val, fahrenheit_val in zip(celsius, fahrenheit):
    print(f"{celsius_val: }\t{fahrenheit_val: }")

