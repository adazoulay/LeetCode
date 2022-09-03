
# Book Sol
def combinations(nums, k):
    def k_combination(curr, start):
        if len(curr) == k:
            result.append(curr[::])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            k_combination(curr, i + 1)
            curr.pop()
        return
    result = []
    k_combination([], 0)
    return result

print(combinations([1,2,3,4,5],2))

# My sol
def compute_k_comb(nums, curr, result, start, k):
    if len(curr) == k:
        result.append(curr[:])
        return
    for i in range(start, len(nums)):
        curr.append(nums[i])
        compute_k_comb(nums, curr, result, i + 1, k)
        curr.pop()
    return

n = [1,2,3,4,5]
r = []

compute_k_comb(n, [], r,0, 2)


print(r)

