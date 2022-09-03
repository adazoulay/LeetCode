import heapq


def online_median(sequence):
    min_heap = []
    max_heap = []
    result = []
    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        result.append(0.5 * (min_heap[0] + (-max_heap[0])))
    return result

seq = [1,2,3,4,5,6,7]

print(online_median(seq))