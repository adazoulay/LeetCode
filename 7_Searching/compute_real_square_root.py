import math

def compute_real_square_root(k):
    left, right = (k, 1.0) if k < 1.0 else (1.0, k)
    while not math.isclose(left, right):
        mid = (left + right) * 0.5
        if mid**2 > k:
            right = mid
        else:
            left = mid
    return left

print(compute_real_square_root(26))