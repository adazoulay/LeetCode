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

def isValidBST(root):
    if not root or (not root.left and not root.right):
        return True
    else:
        left = True
        right = True
        if root.left:
            left = root.left.data < root.data and isValidBST(root.left)
            right = root.right.data > root.data and isValidBST(root.right)
    return left and right

print(isValidBST(A))

def is_binary_tree_bst(tree, low_rage=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_rage <= tree.data <= high_range:
        return False
    return is_binary_tree_bst(tree.left, low_rage, tree.data) and is_binary_tree_bst(tree.right, tree.data, high_range)


def is_binary_tree_bst2(tree):
    QueueEntry = collections.namedtuple("QueueEntry", ('node','lower','upper'))
    bfs_queue = collections.deque([QueueEntry(tree, float('-inf'), float('inf'))])
    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [QueueEntry(front.node.left, front.lower, front.node.data), QueueEntry(front.node.right, front.node.data, front.upper)]
    return True

print(is_binary_tree_bst2(A))