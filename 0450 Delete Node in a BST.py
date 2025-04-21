def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    def dfs(root, key):
        if not root:
            return
        if key < root.val:
            root.left = dfs(root.left, key)
        elif key > root.val:
            root.right = dfs(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            node = root.right
            while node.left:
                node = node.left
            root.val = node.val
            root.right = dfs(root.right, node.val)
        return root

    return dfs(root, key)