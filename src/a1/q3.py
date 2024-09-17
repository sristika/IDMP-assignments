import numpy as np


def find_closest_val(a, v):
    diff = np.abs(a - v)
    idx = np.argmin(diff)
    return a[idx]


# Example
a = np.array([10, 5, 3, 8, 15])
v = 4
closest_val = find_closest_val(a, v)
print(closest_val)
