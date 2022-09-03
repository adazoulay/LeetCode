
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
N.right = M

def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0
    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:
        return partial_path_sum
    return sum_root_to_leaf(tree.left, partial_path_sum ) + sum_root_to_leaf(tree.right, partial_path_sum)

x = sum_root_to_leaf(A)
print(x)