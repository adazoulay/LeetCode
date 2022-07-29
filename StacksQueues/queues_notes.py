# Queues
# Can be implemented using a singly linked list
# 2 Basic operations: enqueue and dequeue


# Deque
# Can be implemented using a doubly linked list
# 4 Basic operations:
# insertion from front: push, insertion from back: inject
# deletion from front: pop, deletion from back eject
import collections


class Queue:
    def __int__(self):
        self._data = collections.deque

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)

# Complexity of enqueue and dequeue O(1)
# max O(n)

# Can be implemented from scratch or use

q = collections.deque()

q.append("e")  # appends element to the right end
q.appendleft("z")  #appends element to the left
q[0]  #retrieves but doesn't remove the element at the front of the queue
q[-1]  #retriev but doesn't remove element at back of queue
q.pop()  #removes element from the right end
q.popleft()  # remove and return element at the left end of the deque

q.extend(["e","f","g"])  #appends multiple values to the right
q.extendleft(["e","f","g"])  #appends multiple values to the left

q.reverse()  #reverses the deque

q.rotate(3)  #shifts elements by arg to the right
