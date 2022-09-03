# ------------------- Combinations ------------------------- #
# https://medium.com/algorithms-and-leetcode/backtracking-with-leetcode-problems-part-2-705c9cc70e52
# Combination: Order does not matter: ex: {1,2,3} and {1,2,3} are NOT two distinct combinations
# nCr = n! / r!*(n-r)!

# Return power set: all subsets
# Given set {1,2,3} and k = 2
# return {1,2}, {1,3}, {2,3}

# Backtracking can be implemented using DFS: path is: [] -> [1] ->[1,2] -> [1,2,3]
# Similar to permutation except one different variable: start: used to track the start index of next candidate instead of used

# Article solution
def C_n_k(a, n, k, start, depth, curr, ans):    # K parameter returns row at k depth in tree
    if depth == k:
        ans.append(curr[::])
        return
    for i in range(start, n):
        curr.append(a[i])
        C_n_k(a, n, k, i + 1, depth + 1, curr, ans)

        curr.pop()
    return

# My sol, removed redundant parameters
def comb(a, k, start, curr, ans):
    if len(curr) == k:
        ans.append(curr[::])
        return
    for i in range(start, len(a)):
        curr.append(a[i])
        comb(a, k, i + 1, curr, ans)
        curr.pop()
    return

a = [1, 2, 3]
n = len(a)
ans = [[None]]
ans = []
ans2 = []
C_n_k(a, n, 2, 0, 0, [], ans)
comb(a, 2, 0, [], ans2)
print(ans2)

# ------------------- Power Set ------------------------- #
# Given a set of distinct integers, return the power set
# [1,2,3] -> [1], [2], [3], [1,2], [2,3], [1,2,3]

def subset(nums):
    result = []

    def dfs(curr, start):
        result.append(curr[:])
        for i in range(start, len(nums)):
            curr.append(nums[i])
            dfs(curr, i+1)
            curr.pop()

    dfs([], 0)
    return result

n = [1,2,3]
print(subset(n))