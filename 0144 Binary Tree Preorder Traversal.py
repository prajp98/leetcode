def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return res