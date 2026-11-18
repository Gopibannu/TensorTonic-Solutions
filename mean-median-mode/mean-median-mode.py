from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    counts  = []
    for i in x:
        counts.append(x.count(i))
    max_e = max(counts)
    index = counts.index(max_e)
    return {"mean": float(np.mean(x)), "median": float(np.median(x)), "mode": float(x[index])}