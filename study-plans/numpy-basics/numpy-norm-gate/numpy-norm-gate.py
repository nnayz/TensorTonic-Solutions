import numpy as np

def norm_gate(X, W, threshold):
    """
    Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed
    """
    X = np.array(X, dtype=np.float64) # (n, d)
    W = np.array(W, dtype=np.float64) # (d, k)

    Z = X @ W # (n, k)
    norms = np.linalg.norm(Z, axis=1) # (n, )
    gate = (norms >= threshold).astype(np.float64)

    return Z * gate[:, np.newaxis]