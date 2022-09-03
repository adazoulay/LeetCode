import bisect

arr = [0,1,2,3,4,5,6,7,8,9,10]
arr2 = [5,6,7,8,9,10,11,12]

# Built in binary search
print(bisect.bisect_left(arr2,9))  # To find first element that is not less that a targeted value
print(bisect.bisect_right(arr2,9))  # To find the first element that is greater than a targeted value