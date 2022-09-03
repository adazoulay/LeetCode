class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


a = ListNode(2)
b = ListNode(1)
c = ListNode(4)
d = ListNode(3)

a.next = b
b.next = c
c.next = d
d.next = None

def printList(node):
    while node:
        print(node.data)
        node = node.next


def insertion_sort(L):  #O(n^2)
    dummy_head = ListNode(0,L)

    while L and L.next:
        if L.data > L.next.data:
            target = L.next
            pre = dummy_head
            while pre.next.data < target.data:
                pre = pre.next
            temp = pre.next
            pre.next = target
            L.next = target.next
            target.next = temp
        else:
            L = L.next
    return dummy_head.next

printList(a)
print(insertion_sort(a))
printList(a)

def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
    tail.next = L1 or L2
    return dummy_head.next

def stable_sort_list(L):
    if not L or not L.next:
        return L
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next
    pre_slow.next = None  #Right before the slow node at the middle, splits list in 2
    return merge_two_sorted_lists(stable_sort_list(L),stable_sort_list(slow))