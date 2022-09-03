
# Binary tree: can either be empty or a root node r linked to a left binary tree and a right binary tree
import collections


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Basic tree traversal, visits every node

A = BinaryTreeNode("A")
B = BinaryTreeNode("B")
C = BinaryTreeNode("C")
D = BinaryTreeNode("D")
E = BinaryTreeNode("E")
F = BinaryTreeNode("F")
G = BinaryTreeNode("G")
H = BinaryTreeNode("H")
I = BinaryTreeNode("I")
J = BinaryTreeNode("J")
K = BinaryTreeNode("K")
L = BinaryTreeNode("L")
M = BinaryTreeNode("M")
N = BinaryTreeNode("N")
O = BinaryTreeNode("O")
P = BinaryTreeNode("P")

A.left, A.right = B, I
B.left, B.right = C, F
C.left, C.right = D, E
F.right = G
G.left = H
I.left, I.right = J, O
O.right = P
J.right = K
K.left, K.right = L, N
L.right = M


def tree_traversal(root):
    if root:
            #Preorder: Processes the root before the traversals of the left and right children
        #print('Preorder: %d' % root.data)
        tree_traversal(root.left)
            #Inorder: Processes the root after the traversal of the left child and before the traversal of the right child
        #print('Inorder: %d' % root.data)
        tree_traversal(root.right)
            #Postorder: Processes the root after the traversals of the left and right children
        #print('Postorder %d' % root.data)

print(tree_traversal(A))

#Inorder traversal: Iterative
def inorderTraversal(root):
    inorder, stack = [], []

    if root is None:
        return inorder

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return inorder

        node = stack.pop()
        inorder.append(node.data)
        root = node.right

    return inorder

print("Inorder", inorderTraversal(A))
# Inorder: <D, C, E, B, F, H, G, A, J, L, M, K, N, I, O, P>


#Preorder traversal: Iterative
def preorderTraversal(root):
    if root is None:
        return
    stack = collections.deque()
    result = []
    stack.append(root)

    while stack:
        curr = stack.pop()
        result.append(curr.data)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return result


print("Preorder", preorderTraversal(A))
# Preorder: <A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P>


def postorderTraversal(root):
    if root is None:
        return
    stack = collections.deque()
    postorder = []
    stack.append(root)

    while stack:
        curr = stack.pop()
        postorder.append(curr.data)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return postorder[::-1]

print("Postorder", postorderTraversal(A))
# Postorder: <D, E, C, H, G, F, B, M, L, N, K, J, P, O, I, A>