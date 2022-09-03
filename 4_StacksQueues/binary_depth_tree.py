
class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right

n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n6 = TreeNode(25)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
n5.right = n6

def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child for curr in curr_depth_nodes for child in (curr.left, curr.right) if child
        ]
    return result

print(binary_tree_depth_order(n1))


# EQUIVALENT TO curr_depth_nodes = [child for curr in curr_depth_nodes for child in (curr.left, curr.right) if child]
#for curr in curr_depth_nodes:
#    for child in (curr.left, curr.right):
#        if child:
#            print(child.data)
