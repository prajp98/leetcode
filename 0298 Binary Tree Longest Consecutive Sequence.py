def longestConsecutive(self, root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node, parent, length):
        nonlocal res
        if not node:
            return
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        res = max(res, length)
        dfs(node.left, node, length)
        dfs(node.right, node, length)

    dfs(root, None, 0)
    return res