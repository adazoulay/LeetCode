def permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A[::])
            return
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result

print(permutations([1,2,3]))


# ----- OR -------

def permutations2(A):
    result = []
    while True:
        result.append(A.copy())
        A = next_permutation(A)
        if not A:
            break
    return result


def next_permutation(perm):
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm

print(permutations2([1,2,3]))