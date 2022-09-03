
# Binary tree: can either be empty or a root node r linked to a left binary tree and a right binary tree

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

# Basic tree traversal, visits every node

A = BinaryTreeNode(314)
B = BinaryTreeNode(6)
C = BinaryTreeNode(271)
D = BinaryTreeNode(28)
E = BinaryTreeNode(0)
F = BinaryTreeNode(561)
G = BinaryTreeNode(3)
H = BinaryTreeNode(17)
I = BinaryTreeNode(6)
J = BinaryTreeNode(2)
K = BinaryTreeNode(1)
L = BinaryTreeNode(401)
M = BinaryTreeNode(641)
N = BinaryTreeNode(257)
O = BinaryTreeNode(271)
P = BinaryTreeNode(28)

A.left, A.right = B, I
B.left, B.right = C, F
C.left, C.right = D, E
F.right = G
G.left = H
I.left, I.right = J, O
O.right = P
J.right = K
K.left, K.right = L, N
L.right = M

def construct_right_sibling(tree):
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            start_node.left.next = start_node.next and start_node.next.left
            start_node = start_node.next
    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left

