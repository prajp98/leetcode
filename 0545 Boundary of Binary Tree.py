def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []

    def isLeaf(node):
        return node and not node.left and not node.right

    def addLeftBoundary(node):
        while node:
            if not isLeaf(node):
                res.append(node.val)
            node = node.left if node.left else node.right

    def addLeaves(node):
        if not node:
            return
        if isLeaf(node):
            res.append(node.val)
            return
        addLeaves(node.left)
        addLeaves(node.right)

    # Right boundary (collected, then reversed)
    def addRightBoundary(node):
        temp = []
        while node:
            if not isLeaf(node):
                temp.append(node.val)
            node = node.right if node.right else node.left
        res.extend(temp[::-1])

    # Root is added only if it's not a leaf
    if not isLeaf(root):
        res.append(root.val)

    addLeftBoundary(root.left)
    addLeaves(root)
    addRightBoundary(root.right)

    return res