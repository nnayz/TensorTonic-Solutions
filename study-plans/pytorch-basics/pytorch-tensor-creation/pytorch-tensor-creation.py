import torch

def create_tensor(method, shape, value=0.0) -> torch.Tensor:
    """
    Returns: list
    """
    if method == "zeros":
        return torch.zeros(shape)
    elif method == "full":
        return torch.full(shape, value)
    return torch.ones(shape)