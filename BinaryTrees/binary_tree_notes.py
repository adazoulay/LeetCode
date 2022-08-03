
# Binary tree: can either be empty or a root node r linked to a left binary tree and a right binary tree

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


def tree_traversal(root):
    if root:
        #Preorder: Processes the root before the traversals of the left and right children
        #print('Preorder: %d' % root.data)
        tree_traversal(root.left)
        #Inorder: Processes the root after the traversal of the left child and before the traversal of the right child
        print('Inorder: %d' % root.data)
        tree_traversal(root.right)
        #Postorder: Processes the root after the traversals of the left and right children
        # print('Postorder %d' % root.data)

tree_traversal(A)