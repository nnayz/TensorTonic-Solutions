import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    np.random.seed(seed)
    return np.random.random(shape) if kind == "uniform" else np.random.standard_normal(shape)
