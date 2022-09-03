
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Basic tree traversal, visits every node

A = BinaryTreeNode(1)
B = BinaryTreeNode(0)
C = BinaryTreeNode(0)
D = BinaryTreeNode(0)
E = BinaryTreeNode(1)
F = BinaryTreeNode(1)
G = BinaryTreeNode(1)
H = BinaryTreeNode(0)
I = BinaryTreeNode(1)
J = BinaryTreeNode(0)
K = BinaryTreeNode(0)
L = BinaryTreeNode(1)
M = BinaryTreeNode(1)
N = BinaryTreeNode(0)
O = BinaryTreeNode(0)
P = BinaryTreeNode(0)

A.left, A.right = B, I
B.left, B.right = C, F
C.left, C.right = D, E
F.right = G
G.left = H
I.left, I.right = J, O
O.right = P
J.right = K
K.left, K.right = L, N
N.right = M

def has_path_sum(tree, remaining_weight):
    if not tree:
        return False
    if not tree.left and not tree.right:
        return remaining_weight == tree.data
    return (has_path_sum(tree.left, remaining_weight - tree.data) or has_path_sum(tree.right, remaining_weight - tree.data))

print(has_path_sum(A, 591))
