import numpy as np

def pairwise_diff(a):
    """Returns: np.ndarray of shape (n, n) where out[i,j] = a[i] - a[j]"""
    a = np.array(a, dtype=np.float64)

    a_row = a.reshape(1, -1)
    a_col = a.reshape(-1, 1)

    return a_col - a_row