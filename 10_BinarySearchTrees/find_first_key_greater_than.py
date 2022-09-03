
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

A = BSTNode(19)
B = BSTNode(7)
C = BSTNode(5)
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


def find_first_greater_than(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if k < subtree.data:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right
    return first_so_far.data

print(find_first_greater_than(A,23))