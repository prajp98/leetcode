def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(root):
        if not root or root == p or root == q:
            return root
        l = dfs(root.left)
        r = dfs(root.right)
        if l and r:
            return root
        return l or r

    return dfs(root)