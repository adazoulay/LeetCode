
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

# My solution, Recur
def BST_LCA(tree,node1,node2):
    if tree == node1 or tree == node2:
        return tree.data
    if node1.data < tree.data < node2.data:
        return tree.data
    elif node1.data < tree.data and node2.data < tree.data:
        return BST_LCA(tree.left, node1, node2)
    else:
        return BST_LCA(tree.right, node1, node2)

print(BST_LCA(A,L,N))

# Book solution, Iter
def find_LCA(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left
    return tree.data

print(find_LCA(A,A,I))