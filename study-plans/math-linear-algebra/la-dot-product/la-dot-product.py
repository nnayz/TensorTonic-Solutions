import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    if not len(x) == len(y):
        raise ValueError("Not possible")

    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]

    return result
        