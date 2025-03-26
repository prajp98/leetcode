def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def dfs(root, l):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val if l else 0
        return dfs(root.left, True) + dfs(root.right, False)

    return dfs(root, False)
