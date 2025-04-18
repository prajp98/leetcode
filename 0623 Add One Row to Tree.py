def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
    if depth == 1:
        return TreeNode(val, left=root)

    def dfs(node, curr_depth):
        if not node:
            return
        if curr_depth == depth - 1:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
        else:
            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)

    dfs(root, 1)
    return root

def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
    if depth == 1:
        return TreeNode(val, left=root)

    queue = deque([root])
    current_depth = 1

    while queue:
        level_size = len(queue)
        if current_depth == depth - 1:
            for _ in range(level_size):
                node = queue.popleft()
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
            break
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        current_depth += 1

    return root