# can_sum(target_sum, numbers)
# Takes in a target sum and array of numbers
# Return array of numbers whose sum = target


# Video brute
# m = target_sum, n = len(numbers)
# O(m * n^m) time, space O(m)
def howSum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        result = howSum(remainder, numbers)
        if result is not None:
            return result + [num]
    return None

print(howSum(7, [2,3])) # Works if you run them one at a time?
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8, [2,3,5]))

# time O(n*m * m), space O(m*m) since array of max len m
def howSum2(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        result = howSum2(remainder, numbers)
        if result is not None:
            memo[target_sum] = result + [num]
            return memo[target_sum]
    memo[target_sum] = None
    return None

# print(howSum2(7, [2,3])) # Works if you run them one at a time?
# print(howSum2(7,[5,3,4,7]))
# print(howSum2(7,[2,4]))
# print(howSum2(8, [2,3,5]))
# print(howSum2(300, [7,14]))

# ------------------------ MY SOL -------------------- #
# My Brute solution, can't use memoization because curr is built in parameter,
def how_sum(target, nums, curr):
    if target == 0:
        return curr
    if target < 0:
        return
    for i in range(len(nums)):
        remaining = target - nums[i]
        curr.append(nums[i])
        if how_sum(remaining, nums, curr):
            return curr
        curr.pop()
    return

#
# print(how_sum(7, [2,3],[])) # Works if you run them one at a time?
# print(how_sum(7,[5,3,4,7],[]))
# print(how_sum(7,[2,4],[]))
# print(how_sum(8, [2,3,5],[]))

def how_sum2(target, nums, curr, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        memo[target] = curr
        return curr
    if target < 0:
        memo[target] = None
        return None
    for i in range(len(nums)):
        remaining = target - nums[i]
        curr.append(nums[i])
        if how_sum2(remaining, nums, curr):
            memo[target] = curr
            return memo[target]
        curr.pop()
    memo[target] = None
    return None

print(how_sum2(7, [2,3],[]))  # Works if you run them one at a time?
print(how_sum2(7,[5,3,4,7],[]))
print('jo', how_sum2(7,[2,4],[]))
print(how_sum2(8, [2,3,5],[]))
print(how_sum2(300, [7,14],[]))