class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

A = BSTNode(19)
B = BSTNode(7)
C = BSTNode(3)
D = BSTNode(2)
E = BSTNode(5)
F = BSTNode(11)
G = BSTNode(17)
H = BSTNode(13)
I = BSTNode(43)
J = BSTNode(23)
K = BSTNode(37)
L = BSTNode(29)
M = BSTNode(31)
N = BSTNode(41)
O = BSTNode(47)
P = BSTNode(53)
A.left, A.right = B, I
B.left, B.right = C, F
C.left, C.right = D, E
F.right = G
G.left = H
I.left, I.right = J, O
J.right = K
K.left, K.right = L, N
L.right = M
O.right = P

# Very efficient data structure
# Efficiently search for a key and find the min and max elements
# Key lookup, insertion and deletion take O(n)=height of tree however,
# However, there are implementations of insert and delete which guarantee height is O(log n)

# Since algo descends tree with each step (O(1)), time complexity is O(h) where h is the height of the tree
def search_bst(tree, key):
    return tree if not tree or tree.data == key else search_bst(tree.left, key) if key < tree.data else search_bst(tree.right, key)

print(search_bst(A, 13))

# Can iterate through elements in sorted order in time O(n)
# Some problems need a combination of a BST and a hash table.
#   Ex: insert student object into BST ordered by GPA. After entered into BST if student GPA or name needs to be edited
#   Would require traversing tree to find, however with the addition of a has table, could find entry directly
# Sometimes necessary to augment a BST to allow it to manipulate more complex data like intervals and support more complex queries like the number of elements in a range
# The BST property is a global property. each node key is greater than left child and smaller than right child

# Use sortedcontainers module but for sake of pedagogy in book, use bintrees module
from sortedcontainers import sortedlist

from bintrees import RBTree

t = RBTree([(5, 'Alfa'), (2, 'Bravo'), (7, 'Charlie'), (3, 'Delta'), (6, 'Echo')])  # Declare tree with array of key value pairs

print(t[2])  # Access element index 2, returns Value
print(t.min_item(), t.max_item())  # Print min, max

t.insert(9, 'Golf')  # Takes in key and value, do NOT pass it as a tuple
t.discard(3)  # Removes element at key index
print(t)

a = t.pop_min()  # returns min element and removes
b = t.pop_max()  # returns max element and removes
print(a, b)
