import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    data = np.array(data, dtype=np.float64)
    lo = np.percentile(data, lo_q, axis=0)
    hi = np.percentile(data, hi_q, axis=0)
    clipped = np.clip(data, lo, hi)
    lo_mask = (data < lo).astype(np.float64)
    hi_mask = (data > hi).astype(np.float64)
    return np.stack([clipped, lo_mask, hi_mask])
    
    