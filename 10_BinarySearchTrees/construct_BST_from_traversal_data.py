
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

# O(n2) if left skewed
def construct_BST(preorder_sequence):
    if not preorder_sequence:
        return None
    i = next((i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence))
    return BSTNode(preorder_sequence[0], construct_BST(preorder_sequence[1:i]), construct_BST(preorder_sequence[i:]))

seq = [43,23,37,29,31,41,47,53]
print(construct_BST(seq))

def rebuild_bst_from_preorder(preorder_sequence):

    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None
        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1
        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)
        return BSTNode(root, left_subtree, right_subtree)

    root_idx = [0]
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))

print(rebuild_bst_from_preorder(seq) == construct_BST(seq))