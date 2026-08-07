#Author: Daniel J. Pierce
#Date: 2026-08-03

import numpy as np

#Create array of intergers from 1 to 20

array = np.arange(1,21)
print(array)

#Print first five elements

print(array[:5])

#Print every second element

print(array[:20:2])

#Print array in reverse

print(array[::-1])

#Print the sum, mean, maximum, and standard deviation

array_sum = np.sum(array)
print(array_sum)

array_mean = np.mean(array)
print(array_mean)

array_max = np.max(array)
print(array_max)

array_min = np.min(array)
print(array_min)

array_std = np.std(array)
print(array_std)

#Create new array containing only values greater than array_mean

comparison = array > array_mean

new_array = array[comparison]
print(new_array)