#Linked List:
# Inserting and deleting are O(1)
# Obtaining Kth element has O(n)

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


#Search
def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

#Insert
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

#Delete
def delete_after(node):
    node.next = node.next.next

a = ListNode('A')
b = ListNode('B')
c = ListNode('C')
d = ListNode('D')

a.next = b
b.next = c
c.next = d
d.next = None

def printList(node):
    while node:
        print(node.data)
        node = node.next

#printList(a)

#REVERSE
def reverse(node):
    temp = node.next.next
    temp2 = node.next
    node.next.next = node
    node.next = None
    helper(temp2, temp)

def helper(node, nextNode):
    if nextNode.next is None:
        nextNode.next = node
        printList(nextNode)
        return nextNode
    temp = nextNode.next
    nextNode.next = node
    helper(nextNode, temp)

#print(reverse(a))

def reverseIter(head):
    prev = None
    curr = head
    while curr:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
    return prev


def reverseRecur(head):
    if not head or not head.next:
        return head
    p = reverseIter(head.next)
    head.next.next = head
    head.next = None
    return p


printList(reverseRecur(a))