import numpy as np

def entropy(p):
    p = np.asarray(p)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))
