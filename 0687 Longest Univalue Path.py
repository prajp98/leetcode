def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node, parent):
        nonlocal res
        if not node:
            return 0
        left = dfs(node.left, node.val)
        right = dfs(node.right, node.val)
        res = max(res, left + right)
        return 1 + max(left, right) if node.val == parent else 0

    dfs(root, None)
    return res