def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    res = 0

    def dfs(root):
        nonlocal res
        if not root:
            return
        dfs(root.right)
        res += root.val
        root.val = res
        dfs(root.left)
        return root

    return dfs(root)