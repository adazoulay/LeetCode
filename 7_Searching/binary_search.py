def binary_search(target, A):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = left + (right - left)/2  # or (left + right)/2 
        if A[mid] < target:
            left = mid + 1
        elif A[mid] > target:
            right = mid - 1
        elif A[mid] == target:
            return mid
    return -1

