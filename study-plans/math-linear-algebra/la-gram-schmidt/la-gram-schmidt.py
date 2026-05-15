import numpy as np

def gram_schmidt(vectors):
    """
    Returns: float64 array of shape (k, n), orthonormal basis spanning the input space.
    """
    A = np.array(vectors, dtype=np.float64)
    Q = np.zeros_like(A)

    for i in range(len(A)): # k
        v = A[i].copy()
        for j in range(i):
            v -= np.dot(v, Q[j]) * Q[j]
        Q[i] = v / np.linalg.norm(v)
    return Q