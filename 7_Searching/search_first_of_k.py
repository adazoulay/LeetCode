def search_first_of_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] < k:
            left = mid + 1
        elif A[mid] == k:
            result = mid
            right = result - 1
    return result

l = [1,2,2,2,3,4,5,6,7,8]
print(search_first_of_k(l, 2))
