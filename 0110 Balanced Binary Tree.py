def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if not root:
            return 0
        lh = dfs(root.left)
        rh = dfs(root.right)
        if lh == -1 or rh == -1 or abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    x = dfs(root)
    return False if x == -1 else True