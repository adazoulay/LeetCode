
def merge_two_sorted_arrays(A,m,B,n):
    a, b, write_index = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1
        write_index -= 1

    while b >= 0:
        A[write_index] = B[b]
        write_index, b = write_index - 1, b - 1
    return A