import numpy as np


def find_local_maxima(a):
    a = np.array(a)

    maxima_mask = (a[1:-1] >= a[:-2]) & (a[1:-1] >= a[2:])

    return a[1:-1][maxima_mask]


# Example
a = np.array([5, 8, 3, 1, 10, 9, 12])
local_maxima = find_local_maxima(a)
print(local_maxima)  # Output: [8, 10]
