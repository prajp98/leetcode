def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def dfs(p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return dfs(p.left, q.right) and dfs(p.right, q.left)

    return dfs(root.left, root.right)
