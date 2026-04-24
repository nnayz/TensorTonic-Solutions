import numpy as np

def outer_sum(a, b):
    """Returns: np.ndarray of shape (m, n), outer sum where out[i,j] = a[i] + b[j]"""

    # Using the standard add.outer

    return np.add.outer(np.array(a, dtype=np.float64), np.array(b, dtype=np.float64))

    # a = np.array(a, dtype=np.float64)
    # b = np.array(b, dtype=np.float64)

    # out = a[:, np.newaxis] + b[np.newaxis, :]
    # return out

    # Another Solution
    
    # res = []
    # for i in range(len(a)):
    #     row_to_app = []
    #     for j in range(len(b)):
    #         row_to_app.append(a[i] + b[j])
    #     res.append(row_to_app)

    # return np.array(res, dtype=np.float64)