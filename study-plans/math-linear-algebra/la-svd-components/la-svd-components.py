import numpy as np

def svd(A):
    """
    Returns: tuple (U, s, Vt) where A = U @ diag(s) @ Vt.
    """
    return np.linalg.svd(np.array(A, dtype=np.float64), full_matrices=False)