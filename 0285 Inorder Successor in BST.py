def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    successor = None
    while root:
        if p.val < root.val:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor