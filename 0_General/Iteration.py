
l = [0,1,2,3,4,5,6,7,8,9]
iterable = iter(l)  # iter(l) returns an iterable of l

# next(iterable, default): default value returned when iterator reaches its end
item = next(iterable, None)  # next(iterable) mutates the value of the iterable, pushes the pointer
print("a",item)  # next(iterable) returns the value of the next iteration. First call returns first value (ar[0])

next(iterable)  # subsequent calls moves pointer to next value
next(iterable)
next(iterable)
item = next(iterable)  # need to reassign as pointer still points to first val
print("b",item)

while iterable:
    try:
        item = next(iterable)
        print(item)
    except StopIteration:   # Trying to iterate past last element raises an error
        break

# itertools
list(zip([1, 2, 3], ['a', 'b', 'c']))  # Takes a number of iterables, returns an iterator over minimum tuples of corresponding args
#[(1, 'a'), (2, 'b'), (3, 'c')]

list(map(sum, zip([1, 2, 3], [4, 5, 6])))  # Can be chained with map
# [5, 7, 9]


# Array of iterators conditionally increment with null check: good example

import heapq

def sort_sorted_arrays(arrays):
    iterArray = [iter(ar) for ar in arrays]
    min_heap = []

    for i, it in enumerate(iterArray):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap,(first_element, i))
    result = []

    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        result.append(smallest_entry)
        smallest_array_iter = iterArray[smallest_array_i]
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result

l2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15,],[16,17,18,19,20]]
#print(sort_sorted_arrays(l2))
