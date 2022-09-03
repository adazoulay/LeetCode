# Traveler on a 2d m*n grid
# Begin in the top left corner, how many ways to get to bottom right
# Can only move up or down

# Brute force: O(2^(n+m)) time, O(n+m) space
def grid_traveler(m,n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)

#print(grid_traveler(1,1))
#print(grid_traveler(2,3))


# Memoized: O(n*m) time, O(n+m) space
def grid_traveler2(m,n, memo={}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler2(m - 1, n, memo) + grid_traveler2(m, n - 1, memo)
    return memo[key]

print(grid_traveler2(18,18))