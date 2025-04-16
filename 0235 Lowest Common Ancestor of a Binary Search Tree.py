def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(root):
        if not root or not p or not q:
            return
        if p.val < root.val and q.val < root.val:
            return dfs(root.left)
        elif p.val > root.val and q.val > root.val:
            return dfs(root.right)
        else:
            return root

    return dfs(root)