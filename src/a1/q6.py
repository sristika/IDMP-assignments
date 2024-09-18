import numpy as np


def check_magic_square(square_matrix):
    size = square_matrix.shape[0]

    if set(square_matrix.ravel()) != set(range(1, size ** 2 + 1)):
        return False

    ref_sum = np.sum(square_matrix[0, :])

    for r in square_matrix:
        if np.sum(r) != ref_sum:
            return False

    for c in square_matrix.T:
        if np.sum(c) != ref_sum:
            return False

    if np.sum(np.diagonal(square_matrix)) != ref_sum:
        return False

    if np.sum(np.diagonal(np.fliplr(square_matrix))) != ref_sum:
        return False

    return True


matrix = np.array([[2, 16, 13, 3],
                   [11, 5, 8, 10],
                   [7, 9, 12, 6],
                   [14, 4, 1, 15]])

print(check_magic_square(matrix))
