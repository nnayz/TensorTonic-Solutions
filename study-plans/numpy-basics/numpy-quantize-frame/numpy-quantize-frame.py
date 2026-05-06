import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    
    data = np.array(data, dtype=np.float64)
    rounded = np.round(data, decimals)
    ceiled = np.ceil(data)
    floored = np.floor(data)

    padded_round = np.pad(rounded, pad_width)
    padded_ceil = np.pad(ceiled, pad_width)
    padded_floored = np.pad(floored, pad_width)

    return np.stack([padded_round, padded_floored, padded_ceil])
    
    