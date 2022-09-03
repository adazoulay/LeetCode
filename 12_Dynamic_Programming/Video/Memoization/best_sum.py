
# Brute force
# m = target_sum, n = len(number)
# O(m*n^m) time, O(m^2)
def bestSum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = bestSum(remainder, numbers)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or (len(combination) < len(shortest_combination)):
                shortest_combination = combination

    return shortest_combination

print(bestSum(7,[7,3,4,7]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))

# O(n*m^2) time, O(m^2) space
def bestSum2(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        memo[target_sum] = None
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = bestSum2(remainder, numbers)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or (len(combination) < len(shortest_combination)):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination


print(bestSum2(7,[7,3,4,7]))
print(bestSum2(8,[2,3,5]))
print(bestSum2(8,[1,4,5]))
print(bestSum2(100,[1,2,5,25]))