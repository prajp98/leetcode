def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(root):
        nonlocal res
        if not root:
            return
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)

    dfs(root)
    return res