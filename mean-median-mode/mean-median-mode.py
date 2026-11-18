from collections import Counter

def mean_median_mode(x: list) -> dict:
    n = len(x)
    
    # 1. Mean: Pure Python sum() is faster than np.mean() for lists
    mean_val = sum(x) / n
    
    # 2. Median: Timsort runs in O(n log n) directly on the list
    s = sorted(x)
    mid = n // 2
    if n % 2 == 1:
        median_val = s[mid]
    else:
        median_val = (s[mid - 1] + s[mid]) / 2.0
        
    # 3. Mode: Counter runs in O(n) in C, replacing the O(n^2) x.count() loop
    mode_val = Counter(x).most_common(1)[0][0]
    
    return {
        "mean": float(mean_val),
        "median": float(median_val),
        "mode": float(mode_val)
    }
