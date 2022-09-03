# This version takes O(n) time and O(n) space
def fib(n):
    table = [0]*(n+1)
    table[1] = 1
    for i in range(2, len(table)):
        table[i] = table[i-1] + table[i-2]
    return table[n]

# This version takes O(n) time and O(1) space
def fibonacci2(n):
    if n <= 1:
        return n
    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1,n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1

print(fibonacci2(6))


print(fib(6))