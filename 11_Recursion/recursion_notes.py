# Euclidian algorithm
def gcd(x,y):
    return x if y == 0 else gcd(y, x % y)

print(gcd(156,36))

# 11_Recursion suitable when the input is expressed using recursive rules
# Good choice for search, enumeration and divide and conquer
# Use recursion as alternative to deeply nested iteration loops
# If asked to remove recursion from a problem, mimic call stack with stack data structure
# 11_Recursion can be easily removed from a tail recursive program by using a while loop (no stack needed)
# If a recursive function may end up being called with the same args more than once, cache the result (Dynamic Prog)
