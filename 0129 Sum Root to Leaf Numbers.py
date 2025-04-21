def sumNumbers(self, root: Optional[TreeNode]) -> int:
    s = 0

    def dfs(node, s):
        if not node:
            return 0
        s = s * 10 + node.val
        if not node.left and not node.right:
            return s
        return dfs(node.left, s) + dfs(node.right, s)

    return dfs(root, 0)