def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


def dutch_flag_partition2(pivot_index, A):
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


def dutch_flag_partition3 (pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


x = [1,2,3,2,2,3,2]
print(x)
dutch_flag_partition3(3,x)
print(x)

