import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """
    if not len(vectors) == len(coefficients):
        raise ValueError("Not possible")

    vectors = np.array(vectors, dtype=np.float64)
    coefficients = np.array(coefficients, dtype=np.float64)

    print(vectors.shape)
    print(coefficients.shape)
    return coefficients @ vectors
    