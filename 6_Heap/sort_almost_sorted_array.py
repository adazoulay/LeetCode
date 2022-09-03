import heapq
import itertools

a = [3, -1, 2, 6, 4, 5, 8]

z = [0,1,2,3,4,5]

def sort_approximately_sorted_array(sequence, k):
    result = []
    min_heap = []

    for x in itertools.islice(sequence,k):
        heapq.heappush(min_heap, x)

    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


print(sort_approximately_sorted_array(a, 2))
