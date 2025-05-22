def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not postorder or not inorder:
        return None
    root = TreeNode(postorder.pop())
    m = inorder.index(root.val)
    root.right = self.buildTree(inorder[m + 1:], postorder)
    root.left = self.buildTree(inorder[:m], postorder)

    return root