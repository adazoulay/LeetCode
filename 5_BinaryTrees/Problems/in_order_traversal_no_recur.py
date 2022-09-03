
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

def inorder_traversal(tree):
    s, result = [],[]
    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            result.append(tree.data)
            tree = tree.right
    return result


def inorder_traversal2(tree):
    path, result = [tree],[]
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result


print(inorder_traversal2(A))