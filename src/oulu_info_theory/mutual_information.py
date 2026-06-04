import numpy as np
from .entropy import entropy

def mi_binary(pxy):
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    return entropy(px) + entropy(py) - entropy(pxy.flatten())
