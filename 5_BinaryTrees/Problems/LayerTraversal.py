def levelOrder(self, root):
    result = []
    if not root:
        return result
    curr_depth_nodes = [root]
    while curr_depth_nodes:
        result.append([curr.val for curr in curr_depth_nodes])
        curr_depth_nodes = [child for curr in curr_depth_nodes for child in (curr.left, curr.right) if child]
    return result
