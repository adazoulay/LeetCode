import heapq

def k_largest_in_array(A,k):
    max_heap = []
    for item in A:
        heapq.heappush(max_heap,item)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return heapq.nlargest(3, max_heap)

print(k_largest_in_array([4,3,2,7,5,32,7,5,22,5,99], 3))