
# Stack: last in first out
# supports push and pop
# When implemented with a linked list: push pop O(1)
# When implemented with an array: push pop O(1)
# Also supports peek: returns top element without deleting it
import collections


def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
        while nodes:
            print(nodes.pop)

# When implementing stack with builtin list:
s = [1, 2, 3, 4, 5]
s[-1]  #Will retrieve top of stack
s.pop()  #removes and returns element at top of stack
len(s) == 0  #tests if stack is empty
# When called on empty stack s[-1] and s.pop cause IndexError

# Implementing Stack from scratch

class Stack:

    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __int__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max())))