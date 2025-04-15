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


def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    closest = root.val
    while root:
        if abs(root.val - target) < abs(closest - target) or \
                (abs(root.val - target) == abs(closest - target) and root.val < closest):
            closest = root.val
        if target < root.val:
            root = root.left
        else:
            root = root.right
    return closest