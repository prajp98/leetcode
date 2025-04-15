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
    res = root.val

    def dfs(node):
        nonlocal res
        if not node:
            return 0
        if abs(target - node.val) == abs(target - res):
            res = min(res, node.val)
        if abs(target - node.val) < abs(target - res):
            res = node.val
        if target < node.val:
            dfs(node.left)
        else:
            dfs(node.right)
    dfs(root)
    return res