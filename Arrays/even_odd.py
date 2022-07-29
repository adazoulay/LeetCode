#Your input is an array of integers, and you have to reorder its entries so that the even entries appear first
#Time complexity: O(n)
#Space complexity 0(1)


def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            # allows to switch items without allocating more memory. Right side happens first
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    print(A)

even_odd([1, 2, 7, 5, 4, 3, 6])
