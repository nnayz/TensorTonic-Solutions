import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    # res = []
    # for val in values:
    #     res.append(3*(val**2) + 2)
    # return res

    x = torch.tensor(values, dtype=torch.float64, requires_grad=True)
    y = ((x ** 3) + (2 * x)).sum()
    y.backward()
    return x.grad.tolist()
