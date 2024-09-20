import numpy as np

# Matrix M and vector v
M = np.array([[4, 2, 1],
              [3, 1, 5],
              [2, 1, 3]])

v = np.array([10, 6, 7])

# (a) Compute the determinant of matrix.
det_M = np.linalg.det(M)
print("Determinant of M:", det_M)

# (b) Check if matrix A is invertible. If it is, find its inverse
if det_M != 0:
    M_inv = np.linalg.inv(M)
    print("Inverse of M:\n", M_inv)
else:
    print("Matrix M is not invertible.")

# (c) Solve the linear system Ax = b for x.
solution = np.linalg.solve(M, v)
print("Solution to Mx = v:\n", solution)

# (d) Compute the eigenvalues and eigenvectors of A.
eig_vals, eig_vecs = np.linalg.eig(M)
print("Eigenvalues of M:", eig_vals)
print("Eigenvectors of M:\n", eig_vecs)

# (e) Verify that the eigenvectors satisfy the equation Av = λv for each eigenvalue λ and eigenvector v
for i in range(len(eig_vals)):
    Mu = np.dot(M, eig_vecs[:, i])
    lambda_u = eig_vals[i] * eig_vecs[:, i]
    print(f"For eigenvalue {eig_vals[i]}:")
    print("Mu:\n", Mu)
    print("λu:\n", lambda_u)
    print("Mu ≈ λu:", np.allclose(Mu, lambda_u))
