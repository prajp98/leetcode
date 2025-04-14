def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    res = float('inf')
    l = []

    def dfs(root):
        if not root:
            return
        dfs(root.left)
        l.append(root.val)
        dfs(root.right)

    dfs(root)
    for i in range(len(l) - 1):
        res = min(res, l[i + 1] - l[i])
    return res