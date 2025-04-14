def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    res = float("inf")
    prev = None

    def dfs(root):
        nonlocal prev, res
        if not root:
            return
        dfs(root.left)
        if prev:
            res = min(res, root.val - prev.val)
        prev = root
        dfs(root.right)

    dfs(root)
    return res
