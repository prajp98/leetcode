def findTilt(self, root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(root):
        nonlocal res
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        res += abs(left - right)
        return root.val + left + right

    dfs(root)
    return res