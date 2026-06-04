import numpy as np

def awgn_capacity(snr_linear):
    return 0.5 * np.log2(1 + snr_linear)
