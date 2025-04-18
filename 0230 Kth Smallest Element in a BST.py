def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    res = 0

    def dfs(root):
        nonlocal k, res
        if not root:
            return
        dfs(root.left)
        k -= 1
        if k == 0:
            res = root.val
            return
        dfs(root.right)

    dfs(root)
    return res