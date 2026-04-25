import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""
    angles = np.array(angles, dtype=np.float64)
    sine = np.sin(angles)
    cosine = np.cos(angles)
    tangent = np.tan(angles)

    return np.vstack([sine, cosine, tangent])