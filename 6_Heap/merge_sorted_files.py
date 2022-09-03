import heapq

def merged_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result

# Pythonic solution
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))

ex = [[1,2,3,4,5],[1,3,6,8,9,76,77],[2,4,7,9,99,243,343]]



print(merged_sorted_arrays(ex))
