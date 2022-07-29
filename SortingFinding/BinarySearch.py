def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        print(mid, arr[mid])
        if arr[mid] == target:
            print("found")
            return mid
        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
    return -1

x = [1,2,5,7,9,25,36,55,60,99, 103, 201, 303]
print(binarySearch(x, 5))

