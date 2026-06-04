import numpy as np

def hamming74_encode(d4):
    d = np.array(d4, dtype=int)
    p1 = d[0]^d[1]^d[3]; p2 = d[0]^d[2]^d[3]; p3 = d[1]^d[2]^d[3]
    return np.array([p1,p2,d[0],p3,d[1],d[2],d[3]])
