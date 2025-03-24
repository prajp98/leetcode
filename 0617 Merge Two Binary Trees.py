def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(p, q):
        if p and q:
            root = TreeNode(p.val + q.val)
            root.left = dfs(p.left, q.left)
            root.right = dfs(p.right, q.right)
            return root
        else:
            return p or q

    return dfs(root1, root2)