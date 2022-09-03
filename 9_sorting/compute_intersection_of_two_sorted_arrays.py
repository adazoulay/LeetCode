
def intersect_two_sorted_array(A, B):
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_A_B






# My solution, does not take advantage of arrays being sorted
def intersect_two_arrays(A,B):
    return set(A).intersection(set(B))



l1 = [2,3,3,5,5,6,7,7,8,12]
l2 = [5,5,6,8,8,9,70,10]
print(intersect_two_sorted_array(l1, l2))



