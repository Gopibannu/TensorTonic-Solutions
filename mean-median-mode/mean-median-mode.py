from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    total = 0
    for i in x:
        total += i
    x = sorted(x)
    if len(x) % 2 ==1:
        median = x[len(x) // 2]
    else:
        median = (x[len(x) // 2] + x[(len(x) // 2) - 1] ) / 2
    counts  = {}
    for i in x:
        counts[i] = counts.get(i, 0) + 1
    mode = None
    max_count = 0
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            mode = num
    return {"mean": float( total / len(x) ), "median": float(median), "mode": float(mode)}