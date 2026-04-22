import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    if operation == "flatten":
        return np.array(data, dtype=np.float64).flatten()
    elif operation == "transpose":
        return np.array(data, dtype=np.float64).T
    else:
        return np.expand_dims(np.array(data, dtype=np.float64), axis=0)