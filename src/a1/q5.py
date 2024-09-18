import numpy as np


def normalize_rows(matrix):
    row_sums = matrix.sum(axis=1, keepdims=True)

    # sum of all elems in a row but still keeping dimensions of original array
    nm = matrix / row_sums

    return nm


# Example
matrix = np.array([[1, 2, 3, 4],
                   [2, 4, 6, 8],
                   [1, 3, 5, 7]])

normalized_matrix = normalize_rows(matrix)
print(normalized_matrix)
