# Does not always yield an optimum solution
# Often the right choice for an optimization problem where there's a natural set of choices to select from
# Easier to conceptualise recursively then implement iteratively for better performance
# Sometimes not obvious

# Common approach is to use invariants
# An invariant is a condition that is true during the execution of a program
# May be based on var values or control logic
#   EX Binary search:
#       Bin search maintains that the space of candidates solutions contains all possible solutions

# Two sum:
arr = [-2,1,2,4,7,11]

def has_two_sum(A,t):
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1
    return False