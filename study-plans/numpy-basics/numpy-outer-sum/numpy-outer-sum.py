import numpy as np

def outer_sum(a, b):
    """Returns: np.ndarray of shape (m, n), outer sum where out[i,j] = a[i] + b[j]"""
    res = []
    for i in range(len(a)):
        row_to_app = []
        for j in range(len(b)):
            row_to_app.append(a[i] + b[j])
        res.append(row_to_app)

    return np.array(res, dtype=np.float64)