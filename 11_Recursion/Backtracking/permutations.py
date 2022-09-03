# ------------------- Permutations ------------------------- #
# https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28
# https://leetcode.com/problems/permutations/discuss/18284/Backtrack-Summary:-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome) for SUMMARY
# Permutation: Order matters: ex: {1,2,3} and {1,2,3} are two distinct permutations
# nPr = n! / (n-r)!

# Given set {1,2,3}
# {1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}

# Backtracking can be implemented using DFS yielding an O(log(n!)) space complexity on the stack, BFS would take n!

# Article solution:
def A_n_k(a, n, k, depth, used, curr, ans):
    if depth == k:
        ans.append(curr[::])  #[::] creates a deep copy
        return
    for i in range(n):
        if not used[i]:
            curr.append(a[i])
            used[i] = True
            print(curr)
            A_n_k(a, n, k, depth+1, used, curr, ans)

            curr.pop()
            print('backtrack:', curr)
            used[i] = False
    return

# My sol, removed redundant parameters
def perm(a, used, curr, ans):
    if all(x is True for x in used):
        ans.append(curr[::])  #[::] creates a deep copy
        return
    for i in range(len(a)):
        if not used[i]:
            curr.append(a[i])
            used[i] = True
            print(curr)
            perm(a, used, curr, ans)

            curr.pop()
            print('backtrack:', curr)
            used[i] = False
    return

# Backtracking visits the implicit vertices in two passes
# Makes problem NP hard time complexity

a = [1,2,3]
n = len(a)
used = [False] * len(a)
ans = [[None]]

ans = []
ans2 = []

A_n_k(a,n,n,0,used,[],ans)
perm(a,used,[],ans2)

print(ans2)

# ---------- Permutations 2 ------------ #
# # Given set {1,1,2}
# # {1,1,2}, {1,2,1}, {2,1,1}

def permuteUnique(nums):
    result = []

    def dfs(curr, elements):
        if len(elements) == 0:
            result.append(curr[:])

        for e in list(set(elements)):
            curr.append(e)
            next_elements = elements[:]
            next_elements.remove(e)
            dfs(curr, next_elements)
            curr.pop()
    dfs([],nums)
    return result

print(permuteUnique([1,2,1]))


# ---------------- Letter combinations --------------------------- #
# Letter combinations of a phone number, Not exactly backtracking but uses elements
#  mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

def letterCombinations(digits):
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def combine(rst, remaining_digits):
        if len(remaining_digits) == 0:
            return rst
        if len(rst) == 0:
            rst = ['']
        nxt_rst = []
        digit = remaining_digits.pop(0)
        for r in rst:
            for c in mapping[digit]:
                nxt_rst.append(r + c)
        return combine(nxt_rst, remaining_digits)  #nxt_rst = r + c

    return combine([],list(digits))

print(letterCombinations("23"))
