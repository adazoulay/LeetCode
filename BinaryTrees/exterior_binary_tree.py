
# Binary tree: can either be empty or a root node r linked to a left binary tree and a right binary tree

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

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

def exterior_binary_tree(tree):
    def is_leaf(node):
        return not node.left and not node.right

    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        return (([subtree] if is_boundary or is_leaf(subtree) else []) +
                left_boundary_and_leaves(subtree.left, is_boundary) + left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left))

    def right_boundary(subtree, is_boundary):
        if not subtree:
            return []
        return (([subtree] if is_boundary and not is_leaf(subtree) else [])
                + right_boundary(subtree.right, is_boundary) + right_boundary(subtree.left, is_boundary and not subtree.right))
    return left_boundary_and_leaves(tree, True) + right_boundary(tree.right, True)

x = (exterior_binary_tree(A))

for y in x:
    print(y.data)
