def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    values = []

    def dfs(node):
        if not node:
            return
        values.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return min(values, key=lambda x: (abs(x - target), x))