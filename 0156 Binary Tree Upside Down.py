def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node, parent, right):
        if not node:
            return parent
        new = dfs(node.left, node, node.right)
        node.right = parent
        node.left = right
        return new

    return dfs(root, None, None)