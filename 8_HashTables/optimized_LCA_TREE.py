def lca(node0, node1):  # !! With parent pointer
    iter0, iter1 = node0, node1
    nodes_on_path = set()
    while iter0 or iter1:
        if iter0:
            if iter0 in nodes_on_path:
                return iter0
        nodes_on_path.add(iter0)
        iter0 = iter0.parent
        if iter1:
            if iter1 in nodes_on_path:
                return iter1
            nodes_on_path.add(iter1)
            iter1 = iter1.parent

