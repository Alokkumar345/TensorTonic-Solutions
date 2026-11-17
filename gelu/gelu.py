import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x=np.array(x)
    erf_values = np.vectorize(math.erf)(x / np.sqrt(2))
    return (x/2)*(1+erf_values)
    