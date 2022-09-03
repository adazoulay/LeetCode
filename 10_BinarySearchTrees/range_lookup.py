import collections

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


# My sol, inefficient, parses whole tree
def range_lookup(tree, low, high):

    def helper(root):
        if root is None:
            return
        if low <= root.data <= high:
            result.append(root.data)
        helper(root.left)
        helper(root.right)
    result = []
    helper(tree)
    return result

print(range_lookup(A,16,42))

def range_lookup2(tree, low, high):

    def helper(root):
        if root is None:
            return
        if root.data > high:
            helper(root.left)
        elif root.data < low:
            helper(root.right)
        else:
            result.append(root.data)
            helper(root.left)
            helper(root.right)
    result = []
    helper(tree)
    return result

print(range_lookup2(A,16,42))