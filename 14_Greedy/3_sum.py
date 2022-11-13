

def has_two_sum(A,t):
    return 0

def has_three_sum(A,t):
    return any(has_two_sum(A, t-a) for a in A)
