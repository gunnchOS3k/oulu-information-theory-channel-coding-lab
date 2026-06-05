import numpy as np

def bsc_capacity(p):
    if p <= 0 or p >= 1: return 0.0
    h = -p*np.log2(p) - (1-p)*np.log2(1-p)
    return 1 - h

def bec_capacity(erasure):
    return 1 - erasure
