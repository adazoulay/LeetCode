# 6_Heap: complete binary tree
# The key at each node is at least as great as the key stored at its children

# Min heap, the key at the root must be less than or equal to its children's key
# Max heap, the key at the root must be greater than or equal the keys of its children

# provided by heapq module
import heapq

l = [1,2,3,4,5,6,7]
k = 3
e = 99
a = 12

heapq.heapify(l)  # Transforms l into a heap, in place
print(heapq.nlargest(k,l))  # Returns the k largest (smallest) elements in L

heapq.heappush(l, e)  # pushes new element to the heap
heapq.heappush(l, (e.key, e))  # pushes new element to the heap, sorted by key value
#  !!! if you want to sort element by a specific attribute in the 6_Heap, use tuple for e ex: heapq.heappush(max-heap, (-star.distance, star))
heapq.heappop(l)  # pops the smallest element of the heap
heapq.heappushpop(l, a)  # pushes a on the heap then pops and returns the smallest element

e = l[0]  # returns the smallest element on the heap without popping it

print()
print(l[0])
print(l[-1])

