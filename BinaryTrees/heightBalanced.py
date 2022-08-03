import collections

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

def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        left_result = check_balanced(tree.left)
        if not left_result.balanced(tree.left):
            return BalancedStatusWithHeight(False, 0)
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = abs(left_result.height - right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    return check_balanced(tree).balanced

print(is_balanced_binary_tree(A))