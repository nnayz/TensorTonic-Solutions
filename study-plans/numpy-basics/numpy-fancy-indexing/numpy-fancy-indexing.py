import numpy as np

def select_by_index(arr, indices, axis):
    """
    Returns: 2D ndarray of float64
    """
    if not (axis == 0 or axis == 1):
        return 
    a = np.array(arr, dtype=np.float64)
    idx = np.array(indices, dtype=np.int64)

    if axis == 0:
        # rows
        return a[idx]
    return a[:, idx]
    