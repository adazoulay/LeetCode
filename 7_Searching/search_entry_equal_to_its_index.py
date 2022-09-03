def search_entry_equal_to_its_index(A):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        elif difference < 0:
            left = mid + 1
    return -1

l = [-2, 0, 2, 3, 6, 7, 9]

print(search_entry_equal_to_its_index(l))