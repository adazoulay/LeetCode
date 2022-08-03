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


def lca(tree, node0, node1):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)
        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            return left_result
        right_result = lca_helper(tree.left, node0, node1)
        if right_result.num_target_nodes == 2:
            return right_result
        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes + int(tree is node0) + int(tree is node1))
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)
    return lca_helper(tree, node0, node1).ancestor.data

print(lca(A,D,E))