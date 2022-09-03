def search_smallest(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left

def search_smallest_with_duplicates(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1
    return left


l = [378, 478, 550, 631, 103, 203, 220, 234, 297, 368]
l2 = [2,2,2, 2,0,1, 2]
print(search_smallest_with_duplicates(l2))
