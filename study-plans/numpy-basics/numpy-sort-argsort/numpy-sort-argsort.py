import numpy as np

def sort_with_indices(data, axis):
    """
    Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices
    """
    arr = np.array(data, dtype=np.float64)
    sorted = np.sort(data, axis=axis)[np.newaxis, :]
    argsorted = np.argsort(data, axis=axis)[np.newaxis, :]
    return np.vstack([sorted, argsorted])