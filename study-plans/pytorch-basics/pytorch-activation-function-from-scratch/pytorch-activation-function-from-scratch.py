import torch


def relu(x) -> torch.Tensor:
    return torch.max(torch.tensor(0), x)

def sigmoid(x) -> torch.Tensor:
    return 1 / (1 + torch.exp(-x))

def tanh(x) -> torch.Tensor:
    return (torch.exp(x) - torch.exp(-x)) / (torch.exp(x) + torch.exp(-x))

def leakyRelu(x) -> torch.Tensor:
    return torch.where(x > 0, x, 1e-2 * x)
    
def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x, dtype=torch.float64)
    if method=="relu":
        return relu(x).tolist()
    elif method=="sigmoid":
        return sigmoid(x).tolist()
    elif method=="tanh":
        return tanh(x).tolist()
    else:
        return leakyRelu(x).tolist()
    