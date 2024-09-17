import numpy as np


def create_array(n, m):
    arr = np.ones((n, m), dtype=int)
    arr[1:-1, 1:-1] = 0

    return arr


# Example
n, m = 5, 6
border_array = create_array(n, m)
print(border_array)
