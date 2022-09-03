

# DP is a general technique for solving optimization, search and counting problems that can be decomposed into Subproblems
# Use DP when you have to make choices to arrive at a solution, can be broken down into sub problems
# Subproblems can reoccur hence need to cache intermediate computations

# Consider computing Fibonacci numbers: [0,1,1,2,3,5,8,13,21]
# F(n) = F(n-1) + F(n-2) where F(0) = 0, F(1) = 1

# This version takes O(n) time and O(n) space
import itertools


def fibonacci(n, cache={}):  # Cache uses one instance for all recursive calls
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n - 2)
    return cache[n]

print(fibonacci(6))

# Minimizing cache space important in DP

# This version takes O(n) time and O(1) space
# Fills cache in a bottom up fashion, allows it to reuse cache storage to reduce the space complexity
def fibonacci2(n):
    if n <= 1:
        return n
    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1,n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1

print(fibonacci2(6))


# Solving DP requires efficiently breaking down problems into subproblems:
#   The origin problem can be solved easily once solutions to sub problems are available
#   The subproblem solutions are cached

# ------------------ MAX SUBARRAY -------------------- #
# Ex: Find the maximum sum over all subarrays of a gain integer arr:
# [904,40,523,12,-335,-385,-124,481,-31]
# Here the max subarray is [0:4]

# The brute force algo (computes every subarray sum) takes O(n^3) time
# Can be improved to O(n^2) at the cost of O(n) storage


def find_maximum_subarray(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(find_maximum_subarray(arr))