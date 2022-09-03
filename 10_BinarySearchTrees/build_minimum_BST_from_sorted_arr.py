class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# My Sol
def build_min_BST(arr):
    if len(arr) == 1:
        return BSTNode(arr[0])
    else:
        mid = len(arr) // 2
        return BSTNode(arr[mid],build_min_BST(arr[0:mid]), build_min_BST(arr[mid+1:])) if len(arr) > 2 else BSTNode(arr[mid],build_min_BST([arr[0]]), build_min_BST([arr[1]]))

l = [0,1,2,3,4,5]
tree = build_min_BST(l)

# Book sol
def build_min_height_bst_from_sorted_array(A):
    def helper(start,end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return BSTNode(A[mid], helper(start, mid), helper(mid + 1, end))
    return helper(0, len(A))

tree2 = build_min_height_bst_from_sorted_array(l)


