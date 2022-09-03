import heapq

def sort_k_increasing_decreasing_array(A):
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or
                (A[i - 1] < A[i] and subarray_type == DECREASING) or (A[i - 1] >= A[i] and subarray_type == INCREASING)):

            sorted_subarrays.append(A[start_idx:i] if subarray_type == INCREASING else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = (DECREASING if subarray_type == INCREASING else INCREASING)
    return merge_sorted_arrays_pythonic(sorted_subarrays)


def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))