def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
    count = 0

    def dfs(root):
        nonlocal count
        if not root:
            return True
        l = dfs(root.left)
        r = dfs(root.right)
        if not l or not r:
            return False
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        count += 1
        return True

    dfs(root)