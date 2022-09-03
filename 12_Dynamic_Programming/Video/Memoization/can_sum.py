# can_sum(target_sum, numbers)
# Takes in a target sum and array of numbers
# Return True if it is possible to generate sum from numbers array
# !!! Repetition allowed

# Brute Force: O(n^m) time, O(m) complexity
def can_sum(target, nums):
    if target == 0:
        return True
    if target < 0:
        return False
    for num in nums:
        remaining = target - num
        if can_sum(remaining, nums):
            return True
    return False

arr = [7,14]
#print(can_sum(300,arr))

# Memo: O(n*m) time, O(m) space
def can_sum2(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for num in nums:
        remaining = target - num
        if can_sum2(remaining, nums):
            memo[remaining] = True
            return True
    memo[remaining] = False
    return False

arr = [7,14]
print(can_sum2(301,arr))