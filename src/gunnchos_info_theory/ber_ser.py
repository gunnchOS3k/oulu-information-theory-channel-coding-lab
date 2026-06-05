import numpy as np

def ber_from_errors(errors, bits):
    return errors / max(bits, 1)
