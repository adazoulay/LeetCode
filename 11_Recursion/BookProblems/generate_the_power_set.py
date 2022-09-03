# Not backtracking
def generate_power_set(nums):
    def directed_power_set(curr, idx):
        if idx == len(nums):
            power_set.append(list(curr))
            return
        directed_power_set(curr, idx + 1)
        directed_power_set(curr + [nums[idx]], idx + 1)

    power_set = []
    directed_power_set([],0)
    return power_set


print(generate_power_set([1,2,3]))

# Backtracking
def powerset(nums):
    result = []

    def dfs(curr, start):
        result.append(curr[:])
        for i in range(start, len(nums)):
            curr.append(nums[i])
            dfs(curr, i + 1)
            curr.pop()

    dfs([], 0)
    return result

print(powerset([1,2,3]))
