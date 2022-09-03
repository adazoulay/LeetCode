# Consider computing Fibonacci numbers: [0,1,1,2,3,5,8,13,21]
# F(n) = F(n-1) + F(n-2) where F(0) = 0, F(1) = 1

# This version takes O(n) time and O(n) space

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1) + fib(n - 2)
    return memo[n]

print(fib(8))